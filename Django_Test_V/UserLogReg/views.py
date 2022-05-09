from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
 #Create your views here.

def LoginView(request):
    current = datetime.now()
    return render(request,"login.html")

def logout_View(request):
    auth.logout(request)
    return redirect("HomePage")

def RegisterView(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username'].strip()
        phonenumber = request.POST['phonenumber'].strip()
        password = request.POST['password'].strip()
        cpassword = request.POST['cpassword'].strip()
        #email = request.post['email'].strip()

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                print("Username already Taken")
            #elif User.objects.filter(email = email).exists():
            #    print("Email already Taken")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User Created Successfully !!!")
                return redirect("login")
        else:
            print("Password didn't match")

    return render(request,"register.html", {})
