from django.shortcuts import render
from main.models import Project

# Create your views here.

def portfolio(request):
    context = {
        'projects': Project.objects.filter(on_portfolio=True).all()
    }

    return render(request, 'portfolio/portfolio.html', context)