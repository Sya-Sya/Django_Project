from django.urls import path
from HomeApp.views import *
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('Home/', views.LandingPage_View, name='Home_View'),
]