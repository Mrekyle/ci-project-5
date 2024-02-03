from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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

        print(message_name)

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

    if request.method == 'POST':
        form = CreateJobPost(request.POST, request.FILES)
        if request.method == 'POST':
            job = form.save()
            messages.success(request, f'Job {job.name} successfully posted.')
            return redirect(reverse('jobs'))
        else:
            messages.error(
                request, f'Oops, something went wrong. Please try again')
    else:
        form = CreateJobPost()

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
            return redirect(reverse('product_detail',))
        else:
            messages.error(request, f'Oops, something has gone wrong. Please try again later. \
                        If the problem persists, please contact support')
    else:
        form = JobPost()
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
            messages.success(request, f'Successfully applied for {job.name}.')
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
