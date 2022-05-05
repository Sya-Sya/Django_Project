from django.urls import path
from HomeApp.views import *

urlpatterns = [
    path('', Home, name='Home')
]