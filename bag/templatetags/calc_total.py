from django import template

register = template.Library()


@register.filter(name='calc_total')
def calc_total(price, quantity):
    """
        Calculates the total price of the items in the bag
    """
    return price * quantity
