from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'projects/projects.html')

def get_project(request, project_article):
    url = 'projects/' + project_article + '.html'
    return render(request, url)