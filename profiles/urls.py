from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderprofile, name='profile'),
    path('admin-dashboard/', views.renderadmin, name='admin'),
    path('delivery-information/', views.renderdelivery,
         name='delivery_information'),
    path('order-history/', views.renderfullhistory, name='order_history'),
    path('order-confirmation/<order_number>',
         views.renderorderhistory, name='order_confirmation'),
    path('product-managment/', views.renderproductmanagment,
         name='product_managment'),
]
