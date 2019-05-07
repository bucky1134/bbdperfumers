from django.db import models

class essential(models.Model):
    title=models.CharField(max_length=200)
    shordesc=models.TextField(blank=True)
    botanicalname=models.TextField(blank=True)
    origin=models.TextField(blank=True)
    longdesc=models.TextField(blank=True)
    price=models.IntegerField()
    variation1=models.TextField(blank=True)
    variation2=models.TextField(blank=True)
    variation3=models.TextField(blank=True)
    variation4=models.TextField(blank=True)
    variation5=models.TextField(blank=True)
    variation6=models.TextField(blank=True)
    variation7=models.TextField(blank=True)
    variation8=models.TextField(blank=True)
    variation9=models.TextField(blank=True)
    maxprice=models.IntegerField(blank=True)
    photo_main=models .ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
    