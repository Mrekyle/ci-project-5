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
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile.html'
    context = {
        'user': profile,
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def renderdelivery(request):
    """
        Renders the users default delivery information
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
