from django.shortcuts import render

# Create your views here.


def rendershop(request):
    """
        Renders the store of the application
    """

    template = 'shop.html'

    context = {

    }

    return render(request, template, context)
