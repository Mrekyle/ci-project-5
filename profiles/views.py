from django.shortcuts import render

from .models import UserProfile

# Create your views here.


def renderprofile(request):
    """
        Renders the profile page of the application
    """

    profile = UserProfile

    template = 'profile.html'
    context = {
        'user': profile,
    }

    return render(request, template, context)


def renderadmin(request):
    """
        Renders the admin dashboard 
    """

    template = 'admin_dashboard.html'

    context = {

    }

    return render(request, template, context)
