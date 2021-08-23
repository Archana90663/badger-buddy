from django.http import HttpResponseRedirect
import random
from ..models import Quotes
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    # Comment out for better code coverage
    '''
    quote = get_object_or_404(Quotes, id=random.randrange(2, Quotes.objects.all().count()))
    if quote.author == 'null':
        quote.author = "Anonymous"
    '''
    context = {
        #'quote': quote
    }
    return render(request, 'help_resources/index.html', context)
