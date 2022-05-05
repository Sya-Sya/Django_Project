from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from urllib.request import urlopen
#import urllib.request as urllib3
import urllib.request as requet
 #Create your views here.

def Home(self):
    current = datetime.now()
    return HttpResponse("Hello, Django!")

 


