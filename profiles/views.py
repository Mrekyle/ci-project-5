from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

from .models import UserProfile
from .forms import UserForm
from checkout.models import Order

# Create your views here.


def renderprofile(request):
    """
        Renders the profile page of the application

        Giving the user quick access to account settings, 
        support, order history quick look and order history overview
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile.html'
    context = {
        'user': profile,
        'form': form,
        'order': orders,
    }

    return render(request, template, context)


def renderdelivery(request):
    """
        Renders the users default delivery information

        Allowing them to update the default for use in
        a quicker smoother checkout
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Delivery information successfully updated.")
            return redirect(reverse('profile'))

    form = UserForm(instance=profile)
    orders = profile.orders.all()

    template = 'delivery_information.html'

    context = {
        'user': profile,
        'form': form,
        'order': orders,
        'on_delivery': True,
    }

    return render(request, template, context)


def renderorderhistory(request, order_number):
    """
        Renders the individual orders history
    """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f"This is a past confirmation for your order {order_number}. \
                 A confirmation email was sent of the date it was ordered.")

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)


def renderfullhistory(request):
    """
        Renders the users full order history in one place
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'full_history.html'

    context = {
        'user': profile,
        'orders': orders,
    }

    return render(request, template, context)


def renderadmin(request):
    """
        Renders the admin dashboard 
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.all()

    template = 'admin_dashboard.html'

    context = {
        'user': profile,
        'orders': orders,
    }

    return render(request, template, context)
