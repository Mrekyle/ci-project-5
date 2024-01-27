from django.db import models

# Create your models here.


class JobPost(models.Model):
    """
        Contains the model for a job posting on the application
    """

    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    job_name = models.CharField(max_length=60, blank=True, null=True)
    job_category = models.ForeignKey(
        'JobCategory', null=True, blank=True, on_delete=models.SET_NULL)
    job_desc = models.TextField()
    job_start = models.DateField(blank=True, null=True)
    job_salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta():
        verbose_name_plural = 'Job Posting'

    def __str__(self):
        return self.job_name


class JobCategory(models.Model):
    """
        Contains job category 
    """

    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Job Category'
