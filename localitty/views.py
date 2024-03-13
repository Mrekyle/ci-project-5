from django.shortcuts import render


def handler404(request, exception):
    """ 
        Renders the error 404 page of the application
    """

    template = 'errors/404.html'

    return render(request, template, status=404)


def handler500(request):
    """ 
        Renders the error 404 page of the application
    """

    template = 'errors/500.html'

    return render(request, template, status=500)
