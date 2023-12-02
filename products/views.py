from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def rendershop(request):
    """
        Renders the store of the application
    """

    products = Product.objects.all()
    template = 'shop.html'
    query = None

    """
        User searching logic 
    """
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'We cant search a blank search. Please enter a valid search request!')
                return redirect(reverse('shop'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'user_search': query,
    }

    return render(request, template, context)


def renderproductdetail(request, product_id):
    """
        Renders the product detail page of the store

        View each products details in full on its own
        individual product page.
    """

    product = get_object_or_404(Product, pk=product_id)

    template = 'product_detail.html'

    context = {
        'product': product
    }

    return render(request, template, context)
