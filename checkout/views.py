from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
# from .models import Order, NewItem
# from products.models import Product
# from bag.contexts import bag_contents
# from profiles.models import UserProfile
# from profiles.forms import UserProfileForm

import stripe
import json

# Create your views here.


def rendercheckout(request):
    """
        Renders the secure checkout of the application

        Also getting all the required information for the user
        to allow them to save there shipping and billing information
    """

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(
            request, f'There is nothing in your bag at the moment. Please add some items to get started')
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def rendercheckout_success(request, order_number):
    """
        Renders the order confirmation page

        Showing that the order was successful, the items in the
        order and the order number
    """

    template = 'checkout_success.html'
    context = {

    }

    return render(request, template, context)
