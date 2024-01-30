from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderindex, name='home'),
    path('support/', views.rendersupport, name='support'),
    path('jobs/', views.renderjobs, name='jobs'),
    path('job_post/', views.renderjobpost, name='job_post'),
    path('job_managment/', views.renderjobmanagment, name='job_managment'),
    path('edit/<int:job_id>/', views.renderjobsedit, name='edit_job'),
    path('delete/<int:job_id>/', views.del_job, name='delete_job'),
    path('apply/', views.renderjob_apply, name='apply'),
    path('applicants/', views.renderjob_applicants, name='applicants'),
    path('roadmap/', views.renderroadmap, name='roadmap'),
]
