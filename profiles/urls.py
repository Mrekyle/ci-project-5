from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderprofile, name='profile'),
    path('admin-dashboard/', views.renderadmin, name='admin'),
    path('delivery-information/', views.renderdelivery, name='delivery_info'),
    path('order-history/', views.renderfullhistory, name='order_history'),
    path('order-history/',
         views.renderorderhistory, name='order_confirmation'),
]
