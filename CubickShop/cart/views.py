from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib.contenttypes.models import ContentType
from collections import Counter

from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm

import os
import py7zr


@require_GET
def cart_add(request, *args,**kwargs):
    ct_model, product_slug, product_size_list = kwargs.get('ct_model'), kwargs.get('slug'), kwargs.get('size').split(',')
    cart = Cart(request)
    content_type = ContentType.objects.get(model=ct_model)
    product = content_type.model_class().objects.get(slug=product_slug)
    cart_product = get_object_or_404(Product, id=product.id)
    for product_size in product_size_list:
        cart.add(product=cart_product, quantity=1, size=product_size)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    print(cart)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request, **kwargs):
    cart = Cart(request).get_cart_info() 
    img_bufer = {}
    for item in cart:
        images_urls = []
        folder_path = cart[item]['product'].image.path[:-3]
        if os.path.exists(folder_path):
            files = os.listdir(folder_path.replace('_',' '))
            for items in files:
                images_urls.append("/media/products/"+cart[item]['product'].image.path.split('/')[-1][:-3].replace('_',' ')+"/" + items)
        else:
            archive = py7zr.SevenZipFile(cart[item]['product'].image.path, mode='r')
            archive.extractall(path='/home/cubik/kubick/CubickShop/media/products/')
            archive.close()
            files = os.listdir(folder_path.replace('_',' '))
            for items in files:
                images_urls.append("/media/products/"+cart[item]['product'].image.path.split('/')[-1][:-3].replace('_',' ')+"/" + items)
        img_bufer[cart[item]['product'].name] = images_urls)
    total_price = Cart(request).get_total_price()
    return render(request, 'cart/detail.html', {'cart': cart, 'total_price': total_price, 'img_url': img_bufer})

@require_GET
def send_order_to_the_email(request, **kwargs):
    cart = Cart(request).get_cart_info() 
    print('________________________')
    print(cart)
    print('________________________')
    return redirect('cart:cart_detail')