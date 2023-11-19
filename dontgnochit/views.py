from django.shortcuts import render

# Create your views here.


def renderdontgnochit(request):
    """
        Renders the dontGnochIt page of the application
    """

    template = 'dontgnochit.html'

    return render(request, template)
