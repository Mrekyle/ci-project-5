from django.contrib import admin
from .models import Products, Category

# Register your models here.


class Admin_Product(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
    )

    ordering = ('sku',)


class Admin_Category(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Products, Admin_Product)
admin.site.register(Category, Admin_Category)
