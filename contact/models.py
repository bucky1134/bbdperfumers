from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    listing=models.CharField(max_length=200)
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    company=models.CharField(max_length=200, blank=True)
    message=models.TextField()
    contact_date=models.DateTimeField(default=datetime.now, blank=True)
    username=models.CharField(max_length=200)
    vendor_comments=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.username
