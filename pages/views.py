from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from contact.models import Contact
from featuredproduct.models import fp
from attars.models import attar
from essentials.models import essential
from aromas.models import aroma
from florals.models import floral
def index(request):
    fps=fp.objects.all()
    context={
        'fps':fps
    } 
    return render(request, 'pages/index.html',context)
# Create your views here.

def about(request):
    return render(request, 'pages/about.html')


def search(request):
    if request.method == 'POST' :
        searchname=request.POST['search']
        essentials = essential.objects.filter(title__icontains=searchname)
        aromas = aroma.objects.filter(title__icontains=searchname)
        attars = attar.objects.filter(title__icontains=searchname)
        florals = floral.objects.filter(title__icontains=searchname)
        mycontext = {
            'mysearch':searchname,
            'essentials':essentials,
            'aromas':aromas,
            'attars':attars,
            'florals':florals
        }
        return render(request, 'pages/search.html',mycontext)

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
    return render(request, 'pages/quality.html')

