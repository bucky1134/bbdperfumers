
from django.urls import path
from . import views

urlpatterns=[
     
    path('Aroma', views.Aroma , name='Aroma'),
    path('<int:ass_id>',views.ass,name='ass'),

]

