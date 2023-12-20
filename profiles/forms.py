from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    """
        Sets the users default shipping information
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
            Adding placeholders and classes to the forms. 

            Removing the auto generated labels and setting the
            autofocus
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'def_phone_number': 'Phone Number',
            'def_street_address1': 'Street Address Line 1',
            'def_street_address2': 'Street Address Line 2',
            'def_town_or_city': 'Town or City',
            'def_county': 'County',
            'def_postcode': 'Postcode',
        }

        self.fields['def_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'def_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
