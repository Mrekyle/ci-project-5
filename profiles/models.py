from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
        Uer profile model that contains the user previous orders,
        payment and shipping information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def_phone_number = models.CharField(max_length=20, null=True, blank=True)
    def_street_address1 = models.CharField(
        max_length=80, blank=True, null=True)
    def_street_address2 = models.CharField(
        max_length=80, blank=True, null=True)
    def_town_or_city = models.CharField(max_length=50, null=True, blank=True)
    def_county = models.CharField(max_length=50, null=True, blank=True)
    def_postcode = models.CharField(max_length=20, blank=True, null=True)
    def_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        """
            Returning the users user name
        """
        return self.user.username


@receiver(post_save, sender=User)
def new_profile(sender, instance, created, **kwargs):
    """
        Allow users to create and update a user profile
    """

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
