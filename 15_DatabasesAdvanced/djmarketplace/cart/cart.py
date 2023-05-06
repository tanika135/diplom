from decimal import Decimal
from django.conf import settings
from app_shop.models import Product, Shop


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, shop_id, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        shop = str(shop_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity':
                    {

                    },
                'price': str(product.price)}

        if update_quantity or shop not in self.cart[product_id]['quantity']:
            self.cart[product_id]['quantity'][shop] = quantity
        else:
            self.cart[product_id]['quantity'][shop] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            for shop, quantity in item['quantity'].items():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * quantity
                item['shop_quantity'] = quantity
                item['shop'] = shop
                yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        total = 0
        for item in self.cart.values():
            total += self.get_item_quantity(item)
        return total

    def get_item_quantity(self, item):
        result = 0
        for shop, quantity in item['quantity'].items():
            result += quantity
        return result

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """

        return sum(Decimal(item['price']) * self.get_item_quantity(item) for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

