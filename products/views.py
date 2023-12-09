from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.


def rendershop(request):
    """
        Renders the store of the application
    """

    products = Product.objects.all()
    template = 'shop.html'
    query = None
    categories = None
    sort = None
    direction = None

    """
        User searching logic 
    """
    if request.GET:
        """
            Search Bar
        """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, f'We cant search a blank search. Please enter a valid search request!')
                return redirect(reverse('shop'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        """
            Shop Page Navigation
        """
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """
            Sorting on shop page filtering
        """
        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'name':
                sorting = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sorting == 'category':
                sorting = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sorting = f'-{sorting}'
            products = products.order_by(sorting)

    sorted = f'{sort}_{direction}'

    context = {
        'products': products,
        'user_search': query,
        'category_filter': categories,
        'sorted': sorted,
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
