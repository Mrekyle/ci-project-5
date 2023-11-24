from django.shortcuts import render

# Create your views here.


def renderprofile(request):
    """
        Renders the profile page of the application
    """

    template = 'profile.html'
    context = {

    }

    return render(request, template, context)
