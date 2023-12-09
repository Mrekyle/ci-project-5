from django.shortcuts import render, redirect

# Create your views here.


def renderbag(request):
    """
        Renders the shopping bag of the application    
    """

    template = 'bag.html'

    context = {

    }

    return render(request, template, context)


def add_bag_items(request, item_id):
    """
        Handles the process of adding items to the
        users shopping bag for checkout
    """

    quantity = int(request.POST.get('quantity'))
    redirection = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    """
        If the item exists in the bags session
        Then the items will be added to the bag
    """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirection)
