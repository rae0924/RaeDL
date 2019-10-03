from django.shortcuts import render
from .models import Tutorial

# Create your views here.

def tutorials(request): 
    context = {'tutorials': Tutorial.objects.all()}
    return render(request, 'tutorials/tutorials.html', context)

def get_tutorial(request, tutorial_article):
    url = 'tutorials/' + tutorial_article + '.html'
    return render(request, url)