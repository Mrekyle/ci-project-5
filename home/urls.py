from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderindex, name='home'),
    path('support/', views.rendersupport, name='support'),
]
