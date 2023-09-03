from django.urls import path
from . import views
from .views import *

urlpatterns = [ 
    path('',views.home,name="home"),
    path('logout/',views.logoutUser,name="logout"),
    path('login/',views.loginUser,name="login"),
    path('upload/',views.upload,name="upload"),
    path('read/<str:t>/',views.read,name="read"),
    path('update/<str:t>/',views.update,name="update"),
    path('delete/<str:t>/',views.delete,name="delete")
]