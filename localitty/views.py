from django.shortcuts import render


def handler404(request, exception):
    """ 
        Renders the error 404 page of the application
    """

    template = '404.html'

    return render(request, template, status=404)
