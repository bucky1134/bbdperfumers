from django.shortcuts import render, redirect 
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
def contact(request):
    if request.method == 'POST':
        pname=request.POST['listing']
        fname=request.POST['fname']
        pageurl=request.POST['pageurl']
        lname=request.POST['lname']
        username=request.POST['username']
        company=request.POST['company']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['message']
        contact=Contact(listing=pname, fname=fname, lname=lname, email=email,
        phone=phone, company=company ,username=username, message=desc)
        contact.save()
        send_mail(
            'Product Inquiry',
            'Hi Rahul\n\n, Below mentioned details are the new Product Inquiries...\n\n'+
            'Name:'+fname+' '+lname+'\n'+
            'UserName:'+username+'\n'+
            'Company:'+company+'\n'+
            'Phone:'+phone+'\n'+
            'Email:'+email+'\n'+
            'Product Query:'+desc+'\n',
            'singhvishal7000@gmail.com',
            ['bbdpefumers@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'your request has been successfully submitted, vendor will get back to you soon in 24 hours')
        return redirect('Account')