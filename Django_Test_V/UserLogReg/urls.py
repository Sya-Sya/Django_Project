from django.urls import path
from UserLogReg.views import *
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('login/', views.LoginView, name='login'),
    re_path('register/', views.RegisterView, name='register'),
]
