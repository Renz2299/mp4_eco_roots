from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from products.models import Product
from .forms import ContactForm

def index(request):
    """ A view to return the index page """

    new_arrivals = Product.objects.filter(category='5')

    bundles = Product.objects.filter(category='6')

    context = {
        'new_arrivals': new_arrivals,
        'bundles': bundles,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """ A view to render the contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully sent your request!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to send your request. Please ensure the form is valid.')
    else:
        form = ContactForm()
        
    context = {
        'form': form,
    }

    return render(request, 'home/contact.html', context)
