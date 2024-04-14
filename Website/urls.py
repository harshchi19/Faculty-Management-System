from django.contrib import admin
from django.urls import path
from Website import views

urlpatterns = [
    path("",views.index, name='index'),
    path("index.html",views.index, name='index'),
    path("profile.html",views.profile, name='profile'),
    path("manage.html",views.manage, name='manage')
]