from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:project_article>', views.get_project, name='project-article')
]