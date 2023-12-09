from django.shortcuts import render

# Create your views here.


def rendercheckout(request):
    """
        Renders the secure checkout of the application
    """

    template = 'checkout.html'

    context = {

    }

    return render(request, template, context)
