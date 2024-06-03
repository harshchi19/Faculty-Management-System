from django.contrib import admin
from django.urls import path
from Website import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index.html", views.index, name='index'),
    path("choice.html", views.choice, name='choice'),
    path("meetourteam.html", views.meetourteam, name='meetourteam'),
    path("institute_login.html", views.institute_login, name='institute_login'),
    path("welcome.html", views.welcome, name='welcome'),
    path("reachus.html", views.reachus, name='reachus'),
    path("home.html", views.home, name='home'),
    
    path("login_faculty.html", views.login_faculty, name='login_faculty'),
    path("profile_faculty.html", views.profile_faculty, name='profile_faculty'),
    path("timetable_faculty.html", views.timetable_faculty, name='timetable_faculty'),
    path("create_leave_application.html", views.create_leave_application, name='create_leave_application'),
    path("leave_application_faculty.html", views.leave_application_faculty, name='leave_application_faculty'),
    path("tools_faculty.html", views.tools_faculty, name='tools_faculty'),
    path("chatroom_faculty.html", views.chatroom_faculty, name='chatroom_faculty'),
    
    path("profile_hod.html", views.profile_hod, name='profile_hod'),
    path("timetable_hod.html", views.timetable_hod, name='timetable_hod'),
    path("leave_application_hod.html", views.leave_application_hod, name='leave_application_hod'),
    path("chatroom_hod.html", views.chatroom_hod, name='chatroom_hod'),
    path("tools_hod.html", views.tools_hod, name='tools_hod'),

    path("checkview", views.checkview, name='checkview'),
    path("send", views.send, name='send'),
    path("getMessages/<str:room>/", views.getMessages, name='getMessages'),
    
    # This should come after static paths to avoid conflicts
    path('<str:room>/', views.room, name='room'),
]
