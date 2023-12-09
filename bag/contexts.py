from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
        Defining the contexts of the users shopping bag

        Giving access to the shopping bag context inside of
        each template. Not just the bag template/view
    """

    bag_items = []
    total_cost = 0
    product_count = 0
    bag = request.session.get('bag', {})

    """
        Calculating the cost of the total number of products

        Based on the quantity of the items in the bag/of a specific
        amount of the sae item in the bag
    """
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total_cost += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
    else:
        product = get_object_or_404(Product, pk=item_id)
        for quantity in item_data['quantity'].items():
            total_cost += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

    """
        Calculating the delivery charges
    """
    if total_cost < settings.FREE_DELIVERY:
        delivery = total_cost * Decimal(settings.STANDARD_DELIVERY_CHARGE)
        free_delivery = settings.FREE_DELIVERY - total_cost
    else:
        delivery = 0
        free_delivery = 0

    grand_total = delivery + total_cost

    context = {

    }

    return context
