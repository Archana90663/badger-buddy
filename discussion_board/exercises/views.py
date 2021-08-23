from django.http import HttpResponseRedirect
import random
from ..models import Quotes, Prompts
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    quote = get_object_or_404(Quotes, id=random.randrange(2, Quotes.objects.all().count()))
    prompt = get_object_or_404(Prompts, id=random.randrange(1, Prompts.objects.all().count()))
    if quote.author == 'null':
        quote.author = "Anonymous"

    context = {
        'quote': quote,
        'prompt': prompt
    }
    return render(request, 'exercises/index.html', context)
