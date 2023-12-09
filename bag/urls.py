from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderbag, name='bag'),
    path('add/<item_id>/', views.add_bag_items, name='add_items'),
    path('adjust/<item_id>/', views.adjust_bag_items, name='adjust_items'),
    path('remove/<item_id>/', views.remove_bag_items, name='remove_items'),
]
