from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("joinus",views.joinuss, name='join us'),
    path("contactus",views.contactus, name='contact us'),
    path("rulesguidelines",views.rulesguidelines, name='rules & guidelines'),
    path("verifiedusers",views.verifiedusers, name='verified users'),
    path("home",views.home, name='home'),
    path("",views.home, name='home')
    
]
