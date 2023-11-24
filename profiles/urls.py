from django.urls import path
from . import views


urlpatterns = [
    path('', views.renderprofile, name='profile'),
]
