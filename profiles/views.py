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
