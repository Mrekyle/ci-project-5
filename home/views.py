from django.shortcuts import render

# Create your views here.


def renderindex(request):
    """
        Renders the home page of the application
    """

    template = 'home/index.html'

    return render(request, template)
