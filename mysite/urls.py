from django.urls import path,re_path
from . import views
from .views import *

urlpatterns = [ 
    path('',views.home,name="home"),
    path('nav/',views.home,name="nav"),
    path('about/',views.about,name="about"),
    path('logout/',views.logoutUser,name="logout"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('upload/',views.upload,name="upload"),
    path('read/<str:id>/',views.read,name="read"),
    re_path(r'^profile/.*/read/(?P<id>\d+)/$', views.read,name="read"),
    path('profile/<str:id>/',views.profile,name="profile"),
    path('update/<str:t>/',views.update,name="update"),
    re_path(r'^profile/.*/update/(?P<t>[a-zA-Z]+)/$', views.update, name='update'),
    path('delete/<str:id>/',views.delete,name="delete"),
    re_path(r'^profile/.*/delete/(?P<id>\d+)/$', views.delete,name="delete"),
    re_path(r'^read/.*/delete_message/(?P<id>\d+)/$', views.delete_message,name="delete_message"),
]