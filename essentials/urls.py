from django.urls import path
from . import views

urlpatterns=[
     path('Essential', views.Essential , name='Essential'),
     path('<int:ess_id>',views.ess,name='ess'),
     path('search',views.search,name='search'),
]

