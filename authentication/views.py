from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import models, User, auth
from django.contrib import messages

from featuredproduct.models import fp



def register(request):
    if request.method == 'POST' :
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is already taken')
                    return redirect('register')
                else:
                    user= User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email,
                    password=password)
                    user.save()
                    messages.success(request,'You are now registered')
                    return redirect('login')
        else:
            messages.error(request,'Password did not match')
            return redirect('register')

    else:
        return render(request,'authentication/register.html')

def login(request):
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            fps=fp.objects.all()
            context={
            'fps':fps
            } 
            return render(request,'pages/index.html',context)
        else:
             messages.error(request,'Invalid Credentials!')
             return redirect('login')
    else:
        return render(request,'authentication/login.html')

def cart(request):
    return render(request,'authentication/cart.html')

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('index')

# Create your views here.
