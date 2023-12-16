import uuid
from django_countries.fields import CountryField

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
        Contains the order information for the order.

        Also allowing the storage of saving a users information
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _gen_order_num(self):
        """
            Generates the unique order number for tracking
        """
        return uuid.uuid().hex.upper()

    def update_total(self):
        """
            Updates the orders grand total each time a new item is added.
            Including the orders delivery costs
        """
        self.order_total = self.newitem.aggregate(Sum('newitem_total'))[
            'newitem_total_sum'] or 0
        if self.order_total < settings.FREE_DELIVERY:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_CHARGE
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
            Overriding the default saving methods

            To set the order number to the order if it
            hadn't been set to the order previously
        """

        if not self.order_number:
            self.order_number = self._gen_order_num()
        super().save(*args, **kwargs)

    def __str__(self):
        """
            Returning the orders order number
        """
        return self.order_number

    class Meta:
        verbose_name_plural = 'Order'


class NewItem(models.Model):
    """
        Checking the items that were added to the order/cart
    """

    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='newitem')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    newitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
            Override the default saving methods to update the new item total
            and to update the orders grand total
        """

        self.newitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

    class Meta:
        verbose_name_plural = 'New Item'
