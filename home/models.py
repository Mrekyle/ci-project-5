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
        verbose_name_plural = 'Job Postings'

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
        verbose_name_plural = 'Job Categories'


class JobApp(models.Model):
    """
        Job Application Model
    """

    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    job = models.ForeignKey(
        JobPost, null=True, blank=True, on_delete=models.SET_NULL)
    resume = models.ImageField(blank=True, null=True)
    cover_letter = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        """
            Returns the applicants name
        """
        return self.name

    class Meta():
        verbose_name_plural = 'Job Applicants'
