from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserForm
from checkout.models import Order

# Create your views here.


@login_required
def renderprofile(request):
    """
        Renders the profile page of the application

        Giving the user quick access to account settings, 
        support, order history quick look and order history overview
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        orders = profile.orders.all()
    else:
        orders = profile.orders.all()

    template = 'profile.html'
    context = {
        'user': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
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
        else:
            messages.error(request, f'Information update has failed, please try again or \
                           contact support for further assistance.')

    form = UserForm(instance=profile)

    template = 'delivery_information.html'

    context = {
        'user': profile,
        'form': form,
        'on_delivery': True,
    }

    return render(request, template, context)


@login_required
def renderorderhistory(request, order_number):
    """
        Renders the individual orders history
    """

    orders = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f"This is a past confirmation for your order {order_number}. \
                 A confirmation email was sent of the date it was ordered.")

    template = 'checkout_success.html'

    context = {
        'orders': orders,
        'from_profile': True
    }

    return render(request, template, context)


@login_required
def renderfullhistory(request,):
    """
        Renders the users full order history in one place
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    p = Paginator(orders, 7)
    page = request.GET.get('page')

    paginate = p.get_page(page)

    template = 'full_history.html'

    context = {
        'user': profile,
        'paginate': paginate,
    }

    return render(request, template, context)


@login_required
def renderadmin(request):
    """
        Renders the admin dashboard 
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    # orders = get_object_or_404(Order)

    # orders = orders.all()

    template = 'admin_dashboard.html'

    context = {
        'user': profile,
        # 'orders': orders,
    }

    return render(request, template, context)
