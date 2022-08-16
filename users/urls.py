"""Defines url patterns for users"""

from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.conf.urls import url
app_name = "users"
urlpatterns = [
    path('login/',
        LoginView.as_view(
            template_name='login.html'
        ),
        name="login"
    ),
    # log out page
    url(r'^logout/$', views.logout_view, name='logout'),
    # registration page
    url(r'^register/$', views.register, name='register'),
]
