from django.db import models

# Create your models here.


class Category(models.Model):
    """
        Category model for the products on sale in the store
    """

    name = models.CharField(max_length=180)
    friendly_name = models.CharField(max_length=180, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Category'


class Product(models.Model):
    """
        Products model for the products on sale in the store
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=180, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Products'
