from core.views import base_view
from django.shortcuts import render

# Create your views here.

@base_view
def index(request, *args, **kwargs):
    return render(request, 'landing/index.html')

@base_view
def about(request, *args, **kwargs):
    return render(request, 'landing/about.html')
