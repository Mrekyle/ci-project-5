from django import forms
from .models import JobPost, JobCategory


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
            if field != 'job_desc':
                if self.fields[field].required:
                    placeholder = f'{placeholders} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
