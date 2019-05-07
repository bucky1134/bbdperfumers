from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from featuredproduct.models import fp
def index(request):
    fps=fp.objects.all()
    context={
        'fps':fps
    } 
    return render(request, 'pages/index.html',context)
# Create your views here.

def about(request):
    return render(request, 'pages/about.html')


def Account(request):
    if request.session._session:
        return render(request,'pages/account.html')
        
    else:
        messages.error(request,'Please Login!')
        return redirect('login')

def mnv(request):
    return render(request, 'pages/mnv.html')

def Quality(request):
    return render(request, 'pages/Quality.html')

