from django.db import models

class aroma(models.Model):
    title=models.CharField(max_length=200)
    shordesc=models.TextField(blank=True)
    longdesc=models.TextField(blank=True)
    origin=models.TextField(blank=True)
    Botanicalname=models.TextField(blank=True)
    price=models.IntegerField()
    maxprice=models.IntegerField(blank=True)
    photo_main=models .ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
    