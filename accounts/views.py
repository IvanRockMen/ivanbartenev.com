from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse

from core.views import base_view



# Create your views here.
@base_view
def register(request, *args, **kwargs):
    return HttpResponse(content="Register")

@base_view
def login(request, *args, **kwargs):
    return HttpResponse(content="Login")

@base_view
def profile(request, *args, **kwargs):
    if(request.user.is_authenticated):
        return HttpResponse(content='Profile')
    else:
        return HttpResponseForbidden(render(request, 'errors/error403.html'))
