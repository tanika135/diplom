from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from app_shops.models import Product, Shop, ShopStock


class CartViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        translation.activate('ru')
        cls.product = Product.objects.create(name='Cart test product')
        cls.shop = Shop.objects.create(name='Cart test shop')
        cls.shopStock = ShopStock.objects.create(
            shop=cls.shop,
            product=cls.product,
            stock=2,
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()
        cls.shop.delete()
        cls.shopStock.delete()

    def test_cart_add(self):

        response = self.client.post(
            reverse('cart:cart_add', kwargs={'product_id': self.product.pk}),
            {
                'shop': self.shop.pk
            }
        )
        self.assertRedirects(response, reverse('cart:cart_detail'))

    def test_cart_detail(self):
        print(reverse('cart:cart_detail'))
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertTemplateUsed(response, 'cart/detail.html')

    def test_cart_remove(self):
        response = self.client.post(
            reverse('cart:cart_remove', kwargs={'product_id': self.product.pk}),
            {}
        )
        self.assertRedirects(response, reverse('cart:cart_detail'))


