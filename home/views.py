from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """

    new_arrivals = Product.objects.filter(category='5')

    bundles = Product.objects.filter(category='6')

    context = {
        'new_arrivals': new_arrivals,
        'bundles': bundles,
    }

    return render(request, 'home/index.html', context)
