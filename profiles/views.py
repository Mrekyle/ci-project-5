from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import UserProfile
from .forms import UserForm
from checkout.models import Order
from products.models import Product

# Create your views here.


@login_required
def renderprofile(request):
    """
        Renders the profile page of the application

        Giving the user quick access to account settings, 
        support, order history quick look and order history overview
    """

    if not request.user.is_authenticated:
        messages.error(request, f'Sorry, you have to be registered to view this page. \
                       Please log in or make an account and try again.')
        return redirect('account_login')

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

    if not request.user.is_authenticated:
        messages.error(request, f'Sorry, you have to be registered to view this page. \
                       Please log in or make an account and try again.')
        return redirect('account_login')

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

    if not request.user.is_authenticated:
        messages.error(request, f'Sorry, you have to be registered to view this page. \
                       Please log in or make an account and try again.')
        return redirect('account_login')

    orders = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f"This is a past confirmation for your order {order_number}. \
                 A confirmation email was sent of the date it was ordered.")

    template = 'checkout_success.html'

    context = {
        'order': orders,
        'from_profile': True
    }

    return render(request, template, context)


@login_required
def renderfullhistory(request,):
    """
        Renders the users full order history in one place
    """

    if not request.user.is_superuser:
        messages.error(
            request, f'Sorry, you dont have access to view this page.')
        return redirect('home')

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-date')

    admin_order = Order.objects.all().order_by('-date')

    p = Paginator(orders, 6)
    page = request.GET.get('page')

    p_a = Paginator(admin_order, 12)
    page_a = request.GET.get('page')

    paginate = p.get_page(page)
    paginate_a = p_a.get_page(page_a)

    template = 'full_history.html'

    context = {
        'user': profile,
        'paginate': paginate,
        'paginate_a': paginate_a,
        'from_admin': True
    }

    return render(request, template, context)


@login_required
def renderadmin(request):
    """
        Renders the admin dashboard 
    """

    if not request.user.is_superuser:
        messages.error(
            request, f'Sorry, you dont have access to view this page.')
        return redirect('home')

    profile = get_object_or_404(UserProfile, user=request.user)
    product = Product.objects.all()
    count = product.count()
    orders = Order.objects.all().order_by('date')
    total_grand_total = Order.objects.aggregate(
        total_grand_total=Sum('grand_total'))
    grand_total_sum = total_grand_total['total_grand_total']

    template = 'admin_dashboard.html'

    context = {
        'user': profile,
        'orders': orders,
        'count': count,
        'grand_total_sum': grand_total_sum
    }

    return render(request, template, context)


@login_required
def renderproductmanagment(request):
    """
        Renders the product managment page
    """

    if not request.user.is_superuser:
        messages.error(
            request, f'Sorry, you dont have access to view this page.')
        return redirect('home')

    product = Product.objects.all()

    p = Paginator(product, 15)
    page = request.GET.get('page')

    paginate = p.get_page(page)

    template = 'product_managment.html'

    context = {
        'products': product,
        'paginate': paginate,
    }

    return render(request, template, context)
