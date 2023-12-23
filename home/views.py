from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

    if request.method == 'POST':
        message_name = request.POST.get['message_name']
        message_email = request.POST.get['message_email']
        message_select = request.POST.get['select_option']
        message_body = request.POST.get['message_body']

        send_mail(
            message_select,
            message_body,
            message_email,
            ['settings.DEFAULT_FROM_EMAIL', 'settings.EMAIL_HOST_USER']
        )

        messages.success(request, f'Thank you {message_name} your message sent successfully. \
                        We will get back to you as soon as we can.')
        return render(request, template)
    else:
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
