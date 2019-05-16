from django.urls import path
from . import views

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forget', views.forget, name='forget'),
    path('logout', views.logout, name='logout'),
    path('changepass', views.changepass, name='changepass'),
]

