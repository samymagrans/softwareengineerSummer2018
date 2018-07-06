# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart

# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += float(x.price)
    
    print(total)
    cart_obj.total = total
    cart_obj.save()
    # print(total)
    return render(request,"carts/home.html", {})

def cart_update(request, *args, **kwargs):
    print(request.POST)
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.add(product_obj)
    else:
        cart_obj.products.remove(product_obj)
    return redirect("cart:home")