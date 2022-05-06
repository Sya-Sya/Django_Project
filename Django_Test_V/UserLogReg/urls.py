from django.urls import path
from UserLogReg.views import *
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('login/', views.LoginView, name='Login'),
    #path('register/', RegisterView, name='Register'),
    #path('logout/', LogiOut, name='Logout')
]
