from django.shortcuts import render

# Create your views here.


def renderbag(request):
    """
        Renders the shopping bag of the application    
    """

    template = 'bag.html'

    context = {

    }

    return render(request, template, context)
