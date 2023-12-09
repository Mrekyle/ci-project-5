from django.shortcuts import render, redirect
from django.urls import reverse

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

    """
        If the item exists in the bags session
        Then the items will be added to the bag
    """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirection)


def adjust_bag_items(request, item_id):
    """
        Handles the user adjusting the items inside of the bag
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    """
        If the item exists in the bags session
        Then the items will be added to the bag
    """
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('bag'))


def remove_bag_items(request, item_id):
    """
        Handles the user removing items from the shopping bag
    """

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('bag'))
