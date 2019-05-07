from django.urls import path
from . import views

urlpatterns=[

    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('Account', views.Account , name='Account'),
    path('mnv', views.mnv , name='mnv'),
    path('Quality', views.Quality , name='Quality'),
   


]