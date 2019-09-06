from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorials, name='tutorials'),
    path('setup', views.setup, name='tutorials-setup'),
    path('venv', views.venv, name='tutorials-venv'),
    path('machine-learning-101', views.machine_learning, name="machine-learning-101")
]