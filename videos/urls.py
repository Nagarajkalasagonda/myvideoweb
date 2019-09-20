from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
   
    path('login',views.login,name='login'),
    path('',views.index),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('create_video',views.create_video),
    path('list_video',views.list_video),
    url(r'^update_video/(?P<pk>[\w{}.-]{1,40})$',views.update_video),
       
]