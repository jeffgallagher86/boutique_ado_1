from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from.forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JZBt7KezzT9QoU1w0388hxRdmeeo5NIz5Nz8TeVTNZX4qLyydgDjR845mIgGPTTf6fJdYfNE2L3pUQRa6W5z25T00yJOwSxAE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
