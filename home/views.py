from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from datetime import date

from .models import JobPost, JobApp
from .forms import CreateJobPost, JobApplication

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
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_select = request.POST.get('select_option')
        message_body = request.POST.get('message_body')

        full_message = f"""
            You have received a message request from {message_name}.
            They need help with - {message_select}.
            ------------------------------------

            {message_body}

            ------------------------------------
            Please reply to {message_email}
        """

        send_mail(
            subject=message_select,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL]
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

    model = JobPost.objects.all().order_by('job_name')

    p = Paginator(model, 6)
    page = request.GET.get('page')
    paginate = p.get_page(page)

    template = 'home/jobs.html'

    context = {
        'job': model,
        'paginate': paginate,
    }

    return render(request, template, context)


@login_required
def renderjobpost(request):
    """
        Renders the job creation form of the application
    """

    if not request.user.is_superuser:
        messages.error(request, f'Sorry you dont have access to this page. \
                       If you believe it is a mistake, please contact us.')
        return redirect(reverse('home'))

    form = CreateJobPost()

    if request.method == 'POST':
        form = CreateJobPost(request.POST, request.FILES)
        if request.method == 'POST':
            job = form.save()
            messages.success(request, f'Job successfully posted.')
            return redirect(reverse('job_managment'))
        else:
            messages.error(
                request, f'Oops, something went wrong. Please try again')
    else:
        form = CreateJobPost()

    job_post = JobPost.objects.all()

    template = 'home/job_post.html'
    context = {
        'form': form,
        'job_post': job_post,
    }

    return render(request, template, context)


@login_required
def renderjobmanagment(request):
    """
        Renders the jobs managment page of the application
    """

    model = JobPost.objects.all().order_by('job_name')
    form = CreateJobPost()

    if not request.user.is_superuser:
        messages.error(
            request, f'Sorry, you dont have access to view this page.')
        return redirect('home')

    p = Paginator(model, 6)
    page = request.GET.get('page')
    paginate = p.get_page(page)

    template = 'home/manage_jobs.html'

    context = {
        'jobs': model,
        'paginate': paginate,
        'form': form,
    }

    return render(request, template, context)


@login_required
def renderjobsedit(request, job_id):
    """
        Renders the edit job page of the app
    """

    if not request.user.is_superuser:
        messages.error(request, f'Sorry you dont have access to this page. \
                       If you believe it is a mistake, please contact us.')
        return redirect(reverse('home'))

    job = get_object_or_404(JobPost, pk=job_id)

    if request.method == 'POST':
        form = CreateJobPost(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Job - {job.job_name}, Successfully Edited.')
            return redirect(reverse('job_managment',))
        else:
            messages.error(request, f'Oops, something has gone wrong. Please try again later. \
                        If the problem persists, please contact support')
    else:
        form = CreateJobPost(instance=job)
        messages.info(request, f'You are currently editing, {job.job_name}.')

    template = 'home/edit_job.html'
    context = {
        'form': form,
        'job': job,
    }

    return render(request, template, context)


@login_required
def del_job(request, job_id):
    """
        Handles the delete methods for jobs on the application
    """

    if not request.user.is_superuser:
        messages.error(request, f"Sorry you dont have access to be here. \
                       Only store owners can do that!")
        return redirect(reverse('home'))

    job = get_object_or_404(JobPost, pk=job_id)
    job.delete()
    messages.success(
        request, f'Job: {job.job_name}, Has been successfully deleted.')

    return redirect(reverse('job_managment'))


def renderjob_apply(request):
    """
        Renders the job application
    """

    jobs = JobPost.objects.all()
    form = JobApplication

    if request.method == 'POST':
        form = JobApplication(request.POST, request.FILES)
        if request.method == 'POST':
            job = form.save()

            """
                Application success sent to admin
            """

            app_date = date.today()
            app_name = form.cleaned_data['name']
            app_email = form.cleaned_data['email']
            app_number = form.cleaned_data['phone_number']
            app_job = form.cleaned_data['job']
            app_cover_letter = form.cleaned_data['cover_letter']
            app_subject = f'New application submitted for: {app_job}'
            send_copy = request.POST.get('send-copy')

            full_message = f"""

            New application submitted for {app_job} on {app_date}
            ------------------------------------------------------
            
            Applicant Details:
            
            Name - {app_name}
            Email - {app_email}
            Phone Number - {app_number}

            ------------------------------------------------------

            Cover Letter:

            {app_cover_letter}

            """

            send_mail(
                subject=app_subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL]
            )

            print(app_job)

            if send_copy == 'on':
                """
                    Sends a copy of the application back to the applicant
                    If they select the option
                """

                applicant_message = f"""

                Thank you for your application. Application submitted for: {app_job} on {app_date}.

                Once our team has had a chance to review your application they will get back 
                to you as soon as they can.
                ------------------------------------------------------
                
                Your Details:
                
                Name - {app_name}
                Email - {app_email}
                Phone Number - {app_number}

                ------------------------------------------------------

                Your Cover Letter:

                {app_cover_letter}

                ------------------------------------------------------

                If something doesn't seem right and you wish to change the information you submitted.
                Or withdraw your application, Please send an email to support@localitty.com.

                """

                send_mail(
                    subject=app_subject,
                    message=applicant_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[app_email]
                )

            messages.success(
                request, f'Application successfully submitted for {app_job}. We will get back to you as soon as we have reviewed your application.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, f'Oops, something went wrong. Please try again')
    else:
        form = JobApplication()

    form = JobApplication
    template = 'job_apply.html'

    context = {
        'form': form,
        'job': jobs,
    }

    return render(request, template, context)


@login_required
def renderjob_applicants(request):
    """
        Renders all job applications made.
    """

    if not request.user.is_superuser:
        messages.error(request, f"Sorry you dont have access to be here. \
                       Only store owners can do that!")
        return redirect(reverse('home'))

    jobs = JobApp.objects.all().order_by('date')

    p = Paginator(jobs, 6)
    page = request.GET.get('page')
    paginate = p.get_page(page)

    template = 'applications.html'

    context = {
        'jobs': jobs,
        'paginate': paginate,
    }

    return render(request, template, context)


@login_required
def del_applicant(request, app_id):
    """
        Handles the delete methods for job applications that 
        have been submitted
    """

    if not request.user.is_superuser:
        messages.error(request, f"Sorry you dont have access to be here. \
                       Only store owners can do that!")
        return redirect(reverse('home'))

    applicant = get_object_or_404(JobApp, pk=app_id)
    applicant.delete()
    messages.success(
        request, f'Job Applicant: {applicant.name}, Has been successfully deleted.')

    return redirect(reverse('applicants'))


def renderroadmap(request):
    """
        Renders the roadmap page of the application
    """

    template = 'home/roadmap.html'

    return render(request, template)


def comingsoon(request):
    """
        Renders a coming soon message
    """

    template = ''

    if request.user.is_superuser:
        messages.info(request,
                      f'Sorry about that, Nothing seems to be there at the moment. Our team are currently working hard to get this up and running. Please check back soon')
        return redirect(reverse('admin'))
    elif request.user:
        messages.info(request,
                      f'Sorry about that, Nothing seems to be there at the moment. Our team are currently working hard to get this up and running. Please check back soon')
        return redirect(reverse('home'))
