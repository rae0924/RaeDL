from django.shortcuts import render
from .models import Tutorial

# Create your views here.

def tutorials(request):
    context = {'tutorials': Tutorial.objects.all()}
    return render(request, 'tutorials/tutorials.html', context)

def setup(request):
    return render(request, 'tutorials/setup.html')

def venv(request):
    return render(request, 'tutorials/venv.html')