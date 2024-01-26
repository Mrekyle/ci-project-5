from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import JobPost
from .forms import Create_Job_Post

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

    model = JobPost
    template = 'home/jobs.html'

    context = {
        'job_post': model
    }

    return render(request, template, context)


@login_required
def renderjobpost(request):
    """
        Renders the jobs page of the application
    """

    if not request.user.is_superuser:
        messages.error(request, f'Sorry you dont have access to this page. \
                       If you believe it is a mistake, please contact us.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = Create_Job_Post(request.POST)
        if request.method == 'POST':
            job = form.save()
            messages.success(request, f'Job {job.name} successfully posted.')
            return redirect(reverse('jobs'))
        else:
            messages.error(
                request, f'Oops, something went wrong. Please try again')
    else:
        form = Create_Job_Post()

    form = Create_Job_Post()
    template = 'home/job_post.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def renderroadmap(request):
    """
        Renders the roadmap page of the application
    """

    template = 'home/roadmap.html'

    return render(request, template)
