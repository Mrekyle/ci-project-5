from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import NewItem


@receiver(post_save, sender=NewItem)
def update_save(sender, instance, created, **kwargs):
    """
        Updates the order total when a new item is created or updated
    """
    print('Update payment signal received')
    instance.order.update_total()


@receiver(post_delete, sender=NewItem)
def update_delete(sender, instance, **kwargs):
    """
        Updates the orders total when an item has been deleted from the order
    """
    print('Delete signal received')
    instance.order.update_total()
