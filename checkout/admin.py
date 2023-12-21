from django.contrib import admin
from .models import Order, NewItem


class ItemAdmin(admin.TabularInline):
    """
        Admin view of the new item model
    """
    model = NewItem
    readonly_fields = ('newitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemAdmin,)

    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'grand_total', 'original_bag', 'stripe_pid')

    fields = ('user_profile', 'order_number', 'date', 'full_name', 'email', 'phone_number', 'county', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2', 'delivery_cost', 'order_total', 'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
