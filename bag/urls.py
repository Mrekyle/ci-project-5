from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderbag, name='bag'),
    path('add/<item_id>/', views.add_bag_items, name='add_items'),
]
