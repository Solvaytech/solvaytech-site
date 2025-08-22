from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def cart_detail(request):
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
    return render(request, 'products/cart_detail.html', {'order': order})

def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart_detail')

def cart_remove(request, id):
    product = get_object_or_404(Product, id=id)
    order = get_object_or_404(Order, user=request.user, is_paid=False)
    order_item = get_object_or_404(OrderItem, order=order, product=product)
    order_item.delete()
    return redirect('cart_detail')

def checkout(request):
    order = get_object_or_404(Order, user=request.user, is_paid=False)
    # Ödeme işlemleri burada gerçekleştirilecek
    order.is_paid = True
    order.save()
    return redirect('product_list')