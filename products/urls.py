from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.rendershop, name='shop'),
    path('<int:product_id>/', views.renderproductdetail, name='product_detail'),
    path('new/', views.rendernewproduct, name='add_product'),
    path('edit/<int:product_id>/', views.renderedit, name='edit_product'),
    path('delete/<int:product_id>/', views.del_product, name='delete_product'),
]
