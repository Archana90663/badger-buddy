from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from ..models import Post, Reply
from .forms import CreatePostForm, CreateReplyForm
from django.views.generic.edit import UpdateView
from django.db.models import Q

# Create your views here.

def index(request):
    posts = Post.objects.all()
    replies = Reply.objects.all()
    context = {
        'posts': posts,
        'replies': replies
    }
    return render(request, 'discussion_board/index.html', context)

def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            details = form.cleaned_data['details']
            anonymous = form.cleaned_data['anonymous']
            p = Post(title=title, details=details, anonymous=anonymous, user=request.user)
            # if want anonmyity, request.user.profile.anonymous
            p.save()
            return HttpResponseRedirect('/board')

    else:
        form = CreatePostForm()

    context = {
        'form': form
    }

    return render(request, 'discussion_board/create-post.html', context)

def create_reply(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_comment = Post.objects.order_by("create_date")
    if request.method == 'POST':
        form = CreateReplyForm(request.POST)
        if form.is_valid():
            details = form.cleaned_data['details']
            anonymous = form.cleaned_data['anonymous']
            r = Reply(post=post, details=details, anonymous=anonymous, user=request.user)
            r.save()
            return HttpResponseRedirect('/board/view-post/' + str(r.post.id))

    else:
        form = CreateReplyForm()

    context = {
        'form': form,
        'post_comment': post_comment
    }

    return render(request, 'discussion_board/create-reply.html', context)


def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    replies = Reply.objects.filter(post=post)
    context = {
        'replies': replies,
        'post': post,
    }

    return render(request, 'discussion_board/view-post.html', context)


def view_reply(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    context = {
        'reply': reply
    }
    return render(request, 'discussion_board/view-reply.html', context)


def delete_post(request, post_id):
    context = {}
    post = get_object_or_404(Post, id=post_id)
    reply = Reply.objects.filter(post=post)
    if request.user == post.user:
        post.delete()
        reply.delete()
    else:
        return HttpResponse('<h1>You are not authorized to delete</h1>')
    return render(request, "discussion_board/delete-post.html", context)


def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user == reply.user:
        reply.delete()
    else:
        return HttpResponse('<h1>You are not authorized to delete</h1>')

    context = {}
    return render(request, 'discussion_board/delete-reply.html', context)

class EditPost(UpdateView):
    model = Post
    fields = ['title', 'details', 'anonymous']
    template_name = 'discussion_board/edit-post.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().user:
            return super(EditPost, self).dispatch(request, *args, **kwargs)
        return HttpResponse('<h1>You are not authorized to edit this post</h1>')

    def get_success_url(self):
        return '/board/view-post/' + str(self.object.id)

class EditReply(UpdateView):
    model = Reply
    fields = ['details', 'anonymous']
    template_name = 'discussion_board/edit-reply.html'

    def dispatch(self, request, *args, **kwargs):   
        if request.user == self.get_object().user:
            return super(EditReply, self).dispatch(request, *args, **kwargs)
        return HttpResponse('<h1>You are not authorized to edit this reply</h1>')

    def get_success_url(self):
        return '/board/view-post/' + str(self.object.post.id)

def search(request):
    # search view based on https://learndjango.com/tutorials/django-search-tutorial
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(details__icontains=query)
    )
    replies = Reply.objects.all()
    context = {
        'posts': posts,
        'replies': replies,
        'query': query,
    }
    return render(request, 'discussion_board/search-results.html', context)