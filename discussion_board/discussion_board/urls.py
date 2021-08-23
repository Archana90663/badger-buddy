from django.urls import path
from . import views

# app_name = 'discussion_board'
urlpatterns = [
    path('', views.index, name='board_index'),
    path('create-post', views.create_post, name='create-post'),
    path('create-reply/<int:post_id>', views.create_reply, name='create-reply'),
    path('view-post/<int:post_id>', views.view_post, name='view-post'),
    path('view-reply/<int:reply_id>', views.view_reply, name='view-reply'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete-post'),
    path('delete-reply/<int:reply_id>', views.delete_reply, name='delete-reply'),
    path('edit-post/<int:pk>', views.EditPost.as_view(), name='edit-post'),
    path('edit-reply/<int:pk>', views.EditReply.as_view(), name='edit-reply'),
    path('search', views.search, name='search-results'),
]
