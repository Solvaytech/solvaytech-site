from django.shortcuts import render
from ecommerce.models import Product  # veya modelin neredeyse oradan

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})
