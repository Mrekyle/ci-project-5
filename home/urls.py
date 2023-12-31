from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderindex, name='home'),
    path('support/', views.rendersupport, name='support'),
    path('jobs/', views.renderjobs, name='jobs'),
    path('roadmap/', views.renderroadmap, name='roadmap'),
]
