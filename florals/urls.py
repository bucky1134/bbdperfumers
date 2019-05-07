from django.urls import path
from . import views

urlpatterns=[
      path('Floural', views.Floral , name='Floural'),
      path('<int:floral_id>',views.floralss,name='floralss'),
]

