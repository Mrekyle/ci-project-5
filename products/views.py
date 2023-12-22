from django.shortcuts import render, reverse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def rendershop(request):
    """
        Renders the store of the application
    """

    products = Product.objects.all().order_by('name').values()
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

    p = Paginator(products, 12)
    page = request.GET.get('page')

    paginate = p.get_page(page)

    context = {
        'products': products,
        'paginate': paginate,
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


@login_required
def rendernewproduct(request):
    """
        Renders the product creation page
    """

    if not request.user.is_superuser:
        messages.error(request, f'Sorry you dont have access to this page. \
                       If you believe it is a mistake, please contact us.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if request.method == 'POST':
            product = form.save()
            messages.success(
                request, f'Product {product.name} Successfully created.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Oops, something has gone wrong. Please try again later. \
                        If the problem persists, please contact support')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def renderedit(request, product_id):
    """
        Renders the edit product page of the app
    """

    if not request.user.is_superuser:
        messages.error(request, f'Sorry you dont have access to this page. \
                       If you believe it is a mistake, please contact us.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Product {product.name} Successfully Edited.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Oops, something has gone wrong. Please try again later. \
                        If the problem persists, please contact support')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing {product.name}.')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def del_product(request, product_id):
    """
        Handles the delete methods for a product on the store
    """

    if not request.user.is_superuser:
        messages.error(request, f"Sorry you dont have access to be here. \
                       Only store owners can do that!")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} Has been successfully deleted.')

    return redirect(reverse('product_managment'))
