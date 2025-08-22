import stripe
from django.shortcuts import render
from .models import Product
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'try',
                'product_data': {'name': 'Test Ürün'},
                'unit_amount': 1000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="https://www.solvaytech.com.tr/payment-success",
        cancel_url="https://www.solvaytech.com.tr/payment-cancel",
    )
    return render(request, 'ecommerce/checkout.html', {'session_id': session.id})
# Create your views here.
