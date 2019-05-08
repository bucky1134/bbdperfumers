from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from contact.models import Contact
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
        user_contacts=Contact.objects.order_by('-contact_date').filter(username=request.user.username)
        context={
            'contacts':user_contacts
        }
        return render(request,'pages/account.html',context)
        
    else:
        messages.error(request,'Please Login!')
        return redirect('login')

def mnv(request):
    return render(request, 'pages/mnv.html')

def Quality(request):
    return render(request, 'pages/Quality.html')

