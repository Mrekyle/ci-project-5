from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderprofile, name='profile'),
    path('admin-dashboard', views.renderadmin, name='admin'),
]
