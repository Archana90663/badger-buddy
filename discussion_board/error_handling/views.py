from django.shortcuts import render

def page_not_found(request, exception):
    return render(request, 'error_handling/404.html')