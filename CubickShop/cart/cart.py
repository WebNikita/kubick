from decimal import Decimal
from django.conf import settings

from shop.models import Product

class Cart(object):
    def __init__(self, request):
        """Инициализация объекта корзины."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем в сессии пустую корзину.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, size ,product, quantity=1, update_quantity=False):
        
        """Добавление товара в корзину или обновление его количества."""
        product_cart_id = f"{str(product.id)}_{size}"
        if product_cart_id not in self.cart:
            self.cart[product_cart_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_cart_id]['quantity'] = quantity
        else:
            self.cart[product_cart_id]['quantity'] += quantity
        if size != 0:
            self.cart[product_cart_id]['size'] = size
        else:
            self.cart[product_cart_id]['size'] = 'None'
        self.save()
    
    def save(self):
        # Помечаем сессию как измененную
        self.session.modified = True
    
    def product_edit_count(self,product_cart_id,count):
        self.cart[product_cart_id]['quantity'] = count
        self.save()

    def remove(self, product, size):
        """Удаление товара из корзины."""
        product_cart_id = f"{str(product.id)}_{size}"
        if product_cart_id in self.cart:
            del self.cart[product_cart_id]
        self.save()
    
    def get_cart_info(self):
        product_ids = []
        product_ids_with_size = self.cart.keys()
        cart = self.cart.copy()
        
        # Получаем объекты модели Product и передаем их в корзину.

        for product_id in product_ids_with_size:
            product = Product.objects.filter(id=int(product_id.split('_')[0]))
            cart[str(product_id)]['product'] = product[0]
        

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        return cart
    
    def __len__(self):
        """Возвращает общее количество товаров в корзине."""
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        print(self.cart)
        print(Decimal(item['price']) * item['quantity']
            for item in self.cart.values())
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
            )
        
    def clear(self):
        # Очистка корзины.
        del self.session[settings.CART_SESSION_ID]
        self.save()
    