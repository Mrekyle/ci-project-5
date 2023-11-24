from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product, Category

# Create your views here.


def rendershop(request):
    """
        Renders the store of the application
    """

    product = Product.objects.all()
    template = 'shop.html'

    context = {
        'products': product
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
