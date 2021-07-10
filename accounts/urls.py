from django.urls import path
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('logout', logout, name="logout")
]
