from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
        Handles the ability for product creation and editing
    """

    class Meta:
        model = Product

        fields = ('name', 'category', 'sku', 'rating', 'price',
                  'description', 'image_url', 'image',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        friendly_names = [(c.id, c.get_friendly_name())
                          for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Chicken Breast - Pack of 4'})
        self.fields['sku'].widget.attrs.update({'placeholder': '123heg4739'})
        self.fields['rating'].widget.attrs.update(
            {'placeholder': 'Set a rating E.G - 4.7'})
        self.fields['price'].widget.attrs.update({'placeholder': '4.89'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Please enter a product description.'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded.0'
