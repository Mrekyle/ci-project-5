from django.contrib import admin
from .models import JobPost, JobCategory, JobApp

# Register your models here


class Admin_Job(admin.ModelAdmin):
    """
        Registers the job Posting
    """

    list_display = (
        'job_name',
        'job_category',
        'job_salary',
        'job_start',
        'job_desc',
    )


class Admin_job_Category(admin.ModelAdmin):
    """
        Registers job category
    """

    list_display = (
        'name',
        'friendly_name',
    )


class Admin_job_App(admin.ModelAdmin):
    """
        Registers job category
    """

    list_display = (
        'name',
        'email',
        'job',
    )


admin.site.register(JobPost, Admin_Job)
admin.site.register(JobCategory, Admin_job_Category)
admin.site.register(JobApp, Admin_job_App)
