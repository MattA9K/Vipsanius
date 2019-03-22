# Author - Matt Andrzejczuk

from django.urls import path
from django.contrib.auth import views as auth_views

import security.views


app_name = "security"
urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]