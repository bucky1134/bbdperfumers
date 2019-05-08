
from django.urls import path
from . import views

urlpatterns=[
     
 path('<int:fps_id>',views.fpsss,name='fpss'),

]

