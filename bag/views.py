from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from products.models import Product
from django.contrib import messages

# Create your views here.


def renderbag(request):
    """
        Renders the shopping bag of the application    
    """

    template = 'bag.html'

    context = {

    }

    return render(request, template, context)


def add_bag_items(request, item_id):
    """
        Handles the process of adding items to the
        users shopping bag for checkout
    """

    quantity = int(request.POST.get('quantity'))
    redirection = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    product = Product.objects.get(pk=item_id)

    """
        If the item exists in the bags session
        Then the items will be added to the bag
    """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Added {bag[item_id]} of {product.name} to your bag!')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag

    return redirect(redirection)


def adjust_bag_items(request, item_id):
    """
        Handles the user adjusting the items inside of the bag
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = Product.objects.get(pk=item_id)

    """
        If the item exists in the bags session
        Then the items will be added to the bag
    """
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag!')

    request.session['bag'] = bag

    return redirect(reverse('bag'))


def remove_bag_items(request, item_id):
    """
        Handles the user removing items from the shopping bag
    """

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f"Product successfully removed from bag")

        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, f'Error removing item: {e}. If the problem persists, please contact support')
        return HttpResponse(status=500)
