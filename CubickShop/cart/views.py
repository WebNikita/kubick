from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib.contenttypes.models import ContentType
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_GET
def cart_add(request, *args,**kwargs):
    print(kwargs)
    ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
    cart = Cart(request)
    content_type = ContentType.objects.get(model=ct_model)
    product = content_type.model_class().objects.get(slug=product_slug)
    cart_product = get_object_or_404(Product, id=product.id)
    cart.add(product=cart_product)
    print(cart)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})