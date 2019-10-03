from django.urls import path 
from . import views

urlpatterns = [
    path('', views.tutorials, name='tutorials'),
    path('<str:tutorial_article>/', views.get_tutorial, name='tutorial-article'),
]