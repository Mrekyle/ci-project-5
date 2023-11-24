from django.shortcuts import render

# Create your views here.


def renderindex(request):
    """
        Renders the home page of the application
    """

    template = 'home/index.html'

    return render(request, template)


def rendersupport(request):
    """
        Renders the support page of the application
    """

    template = 'home/support.html'

    return render(request, template)


def renderjobs(request):
    """
        Renders the jobs page of the application
    """

    template = 'home/jobs.html'

    return render(request, template)


def renderroadmap(request):
    """
        Renders the roadmap page of the application
    """

    template = 'home/roadmap.html'

    return render(request, template)
