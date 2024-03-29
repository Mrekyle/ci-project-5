from django import forms
from .models import JobPost, JobCategory, JobApp


class CreateJobPost(forms.ModelForm):
    """
        Creates the form for the job posting to be created.
    """
    class Meta():
        model = JobPost
        exclude = ('user',)
        fields = ('job_name', 'job_category',
                  'job_salary', 'job_start', 'job_desc',)

    def __init__(self, *args, **kwargs):
        """
            Set form classes, labels and autofocus
        """

        super().__init__(*args, **kwargs)
        category = JobCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly()) for c in category]

        placeholders = {
            'job_name': 'Job Name',
            'job_category': 'Job Category',
            'job_salary': 'Job Starting Salary',
            'job_start': 'Job Expected Start Date',
        }

        self.fields['job_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields['job_category'].choices = friendly_names
            self.fields['job_salary'].widget.attrs.update(
                {'placeholder': 'Job Salary'})
            self.fields['job_start'].widget.attrs.update(
                {'placeholder': 'Job Start Date - MM/DD/YYY'})
            if field != 'job_desc':
                if self.fields[field].required:
                    placeholder = f'{placeholders} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False


class JobApplication(forms.ModelForm):
    """
        Job application form 
    """

    class Meta():
        model = JobApp
        fields = {'name', 'email', 'phone_number',
                  'job', 'cover_letter', 'resume'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': '', 'required': '', 'placeholder': 'Your Name *'})
        self.fields['email'].widget.attrs.update(
            {'class': '', 'required': '', 'placeholder': 'Your Email Address *'})
        self.fields['phone_number'].widget.attrs.update(
            {'class': '', 'required': '', 'placeholder': 'Your Phone Number *'})
        self.fields['job'].widget.attrs.update({'class': '', 'required': ''})
        self.fields['cover_letter'].widget.attrs.update(
            {'class': 'form-control testing', 'rows': '8', 'placeholder': 'Tell Us About Yourself'})
        self.fields['resume'].widget.attrs.update(
            {'class': '', 'required': ''})
