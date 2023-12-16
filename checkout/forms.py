from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
        Generates an order form specific to the required
        information
    """

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode', 'country', 'county')

    def __init__(self, *args, **kwargs):
        """
            Adds placeholders and classes to the form
            for a better UI experience

            Removes automatically generated labels
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Address Line 1',
            'street_address2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Zip/Postcode'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        """
            Setting the placeholders for the forms inputs fields
        """
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
