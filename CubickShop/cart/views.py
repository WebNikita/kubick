from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib.contenttypes.models import ContentType
from collections import Counter

from django.conf import settings
from django.core.mail import send_mail

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
    print(product_size_list)
    if '0' not in product_size_list: 
        for product_size in product_size_list:
            cart.add(product=cart_product, quantity=int(product_size.split('|')[1]), size=product_size.split('|')[0])
    else:
        cart.add(product=cart_product, quantity=1, size='0')
    return redirect('cart:cart_detail')

@require_GET
def add_product_count(request):
    get_data = request.GET
    cart = Cart(request)
    print(get_data['count'])
    product_id, count = f"{get_data['product_id']}", int(get_data['count'])
    cart.product_edit_count(product_id,count)

    return redirect('cart:cart_detail')


def cart_remove(request, product_id, size):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product, size)
    return redirect('cart:cart_detail')

def cart_detail(request, **kwargs):
    cart = Cart(request).get_cart_info() 
    img_bufer = {}
    for item in cart:
        images_urls = []
        try:
            folder_path = cart[item]['product'].image.path[:-3]
            if os.path.exists(folder_path):
                files = os.listdir(folder_path.replace('_',' '))
                for items in files:
                    images_urls.append("/media/products/"+cart[item]['product'].image.path.split('/')[-1][:-3].replace('_',' ')+"/" + items)
                images_urls.sort()
            else:
                archive = py7zr.SevenZipFile(cart[item]['product'].image.path, mode='r')
                archive.extractall(path='/home/cubik/kubick/CubickShop/media/products/')
                archive.close()
                files = os.listdir(folder_path.replace('_',' '))
                for items in files:
                    images_urls.append("/media/products/"+cart[item]['product'].image.path.split('/')[-1][:-3].replace('_',' ')+"/" + items)
                images_urls.sort()
        except Exception as e:
            print(e)
        img_bufer[cart[item]['product'].name] = images_urls
    total_price = Cart(request).get_total_price()
    return render(request, 'cart/detail.html', {'cart': cart, 'total_price': total_price, 'img_url': img_bufer})

@require_GET
def send_order_to_the_email(request, **kwargs):
    counter = 0
    user_info = request.GET
    cart = Cart(request).get_cart_info() 
    message_body = f'Новый заказ от {user_info["name"]}\nТел: {user_info["phone"]}\nEmail: {user_info["email"]}\nДетали заказа:\n-------------------\n'
    for item in cart:
        counter += 1
        message_body += f'{counter}. Наименование позиции: {cart[item]["product"].name}\nАртикул: {cart[item]["product"].article}\nКол-во: {cart[item]["quantity"]}\nРазмер: {cart[item]["size"]}\n-------------------\n'
    send_mail('Новый заказ', message_body, settings.EMAIL_HOST_USER, ['matik007@yandex.ru'])
    counter = 0
    message_body = f'Здравствуйте {user_info["name"]}, ваше обращение зарегистрировано!\nСкоро с вами свяжутся!\nВаш заказ:\n'
    for item in cart:
        counter += 1
        message_body += f'{counter}. Наименование позиции: {cart[item]["product"].name}\nАртикул: {cart[item]["product"].article}\nКол-во: {cart[item]["quantity"]}\nРазмер: {cart[item]["size"]}\n-------------------\n'
    try:
        send_mail('Успешный запрос',message_body, settings.EMAIL_HOST_USER, [user_info["email"]])
        Cart(request).clear()
    except Exception as e:
        pass
    return redirect('cart:cart_detail')