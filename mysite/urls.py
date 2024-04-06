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
    re_path(r'^profile/.*/update/(?P<t>[\w\s]+)/$', views.update, name='update'),
    path('delete/<str:id>/',views.delete,name="delete"),
    re_path(r'^profile/.*/delete/(?P<id>\d+)/$', views.delete,name="delete"),
    re_path(r'^read/.*/delete_message/(?P<id>\d+)/$', views.delete_message,name="delete_message"),
    path('discussion/list/', views.discussion_list, name='discussion_list'),
    path('discussion/create/', views.discussion_create, name='discussion_create'),
    path('discussion/<str:id>/', views.discussion_detail, name='discussion_detail'),
    path('discussion/update/<str:t>/', views.discussion_update, name="discussion_update"),
    path('discussion/delete/<str:id>/', views.discussion_delete, name="discussion_delete"),
    re_path(r'^discussion/(?P<discussion_id>\d+)/delete_message/(?P<id>\d+)/$', views.delete_discussion_message, name="delete_discussion_message"),
]