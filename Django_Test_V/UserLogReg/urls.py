from django.urls import path
from UserLogReg.views import *
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('login/', views.LoginView, name='Login'),
    #path('register/', RegisterView, name='Register'),
    #path('logout/', LogiOut, name='Logout')
]
