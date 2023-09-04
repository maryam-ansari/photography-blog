from django.urls import path,re_path
from . import views
from .views import *

urlpatterns = [ 
    path('',views.home,name="home"),
    path('logout/',views.logoutUser,name="logout"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('upload/',views.upload,name="upload"),
    path('read/<str:t>/',views.read,name="read"),
    path('update/<str:t>/',views.update,name="update"),
    path('delete/<str:t>/',views.delete,name="delete"),
    #path('delete_message/<str:id>/',views.delete_message,name="delete_message")
   re_path(r'^read/.*/delete_message/(?P<id>\d+)/$', views.delete_message,name="delete_message"),
]