from django import forms
from .models import JobPost, JobCategory


class Create_Job_Post(forms.ModelForm):
    """
        Creates the form for the job posting to be created.
    """
    class Meta():
        model = JobPost

        fields = ('job_name', 'job_category',
                  'job_salary', 'job_start', 'job_desc')

    def __init__(self, *args, **kwargs):
        """
            Set form classes, labels and autofocus
        """

        super().__init__(*args, **kwargs)
        category = JobCategory.objects.all()

        friendly_names = [(c.id, c.get_friendly()) for c in category]

        self.fields['job_category'].choices = friendly_names

        labels = {
            'job_name': 'Job Name',
            'job_category': 'Job Category',
            'job_salary': 'Job Expected Salary',
            'job_date': 'Job Expected Start Date',
        }

        self.fields['job_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'job_desc':
                if self.fields[field].required:
                    label = f'{labels} *'
                else:
                    label = labels[field]
                self.fields[field].widget.attrs['label'] = label
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
