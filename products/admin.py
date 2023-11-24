from django.contrib import admin
from .models import Product, Category

# Register your models here.


class Admin_Product(admin.ModelAdmin):
    """
        Product Admin
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
    )

    ordering = ('sku',)


class Admin_Category(admin.ModelAdmin):
    """
        Category Admin
    """
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Product, Admin_Product)
admin.site.register(Category, Admin_Category)
