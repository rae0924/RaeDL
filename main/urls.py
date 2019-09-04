from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='raedl-home'),
    path('about/', views.about, name='raedl-about'),
    path('tutorials/', include('tutorials.urls')),
    path('portfolio/', include('portfolio.urls')),
]