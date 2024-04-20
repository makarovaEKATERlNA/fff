from django.contrib import admin
from django.urls import path
import myproject.views

urlpatterns = [
    path("",myproject.views.index),
    path("login", myproject.views.login)
]
