from home import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
]
