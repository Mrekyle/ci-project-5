from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.rendershop, name='shop'),
    path('<int:product_id>/', views.renderproductdetail, name='product_detail'),
]
