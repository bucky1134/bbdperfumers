from django.urls import path
from . import views

urlpatterns=[
     path('Attar', views.Attar , name='Attar'),
     path('<int:attarss_id>',views.attarss,name='attarss'),
]

