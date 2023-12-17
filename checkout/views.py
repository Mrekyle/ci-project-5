from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, NewItem
from products.models import Product
from bag.contexts import bag_contents
# from profiles.models import UserProfile
# from profiles.forms import UserProfileForm

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
        Handles the data from the users checkout procedure.
        Storing data for later use
    """

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save-info': request.POST.get('save-info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Oops that isn't look right..."
                       " Please try again later or contact support for further assistance.")
        return HttpResponse(content=e, status=400)


def rendercheckout(request):
    """
        Renders the secure checkout of the application

        Also getting all the required information for the user
        to allow them to save there shipping and billing information

        Handles what happens when a user submits the form
        Handles what happens if there is an error anywhere along the way
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line = NewItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line.save()
                except Product.DoesNotExist:
                    messages.error(request, f'One of the products in your bag does not exist on our database. \
                                   Please contact us for assistance in getting this fixed.')
                    order.delete()
                    return redirect(reverse('bag'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, f'Oops the order form was not valid. Please take another look and try again. \
                      If the problem persists, please contact support')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, f'There is nothing in your bag at the moment. \
                      Please add some items to get started')
            return redirect(reverse('shop'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(
            request, f'No stripe public key. Please set it in the environment variables')

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def rendercheckout_success(request, order_number):
    """
        Renders the order confirmation page

        Showing that the order was successful, the items in the
        order and the order number

        Telling the user that a confirmation email will
        be sent shortly
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully submitted! \
                    Your order number is {order_number} \
                    A confirmation email will be sent to \
                    {order.email}')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout_success.html'
    context = {
        'order': order,
        'save-info': save_info,
    }

    return render(request, template, context)
