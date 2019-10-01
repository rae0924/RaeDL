from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorials, name='tutorials'),
    path('<str:article>/', views.get_article, name='article'),
]