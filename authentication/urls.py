from django.urls import path
from . import views

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('logout', views.logout, name='logout'),
]

