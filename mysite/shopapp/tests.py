from string import ascii_letters
from random import choices

from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from shopapp.models import Product, Order
from shopapp.utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(6, 3)
        self.assertEquals(result, 9)


class ProductCreateViewTestCase(TestCase):

    def setUp(self) -> None:
        self.product_name = ''.join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        response = self.client.post(
            reverse('shopapp:product_create'),
            {
                'name': self.product_name,
                'price': '400',
                'description': 'A good table',
                'discount': '10',
            }
        )
        self.assertRedirects(response, reverse('shopapp:products_list'))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertEquals(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'products-fixtures.json',
        'auth-fixtures.json',

    ]

    def test_products(self):
        response = self.client.get(reverse('shopapp:products_list'))
        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)
        # products = Product.objects.filter(archived=False).all()
        # products_ = response.context['products']
        # for p, p_ in zip(products, products_):
        #     self.assertEquals(p.pk, p_.pk)

        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context['products']),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='bob_test', password='qwerty')
        permission_view_order = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission_view_order)
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()
        cls.product.delete()
        cls.order.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        __class__.order = Order.objects.create(
            delivery_address='Test',
            promocode='10Test',
            user=self.user
        )
        __class__.order.products.set([self.product])

    # def test_create_order(self):
    #     response = self.client.post(
    #         reverse('shopapp:create_order'),
    #         {
    #             'delivery_address': 'Test',
    #             'promocode': '10test',
    #             'user': self.user.id,
    #             'products': [self.product.id],
    #         }
    #     )
    #     self.assertRedirects(response, reverse('shopapp:orders_list'))
        # self.assertTrue(
        #     Order.products.filter(name=self.).exists()
        # )

    # def tearDown(self) -> None:
    #     self.objects.delete()

    def test_order_details(self):
        response = self.client.get(
            reverse('shopapp:order_details', kwargs={'pk': __class__.order.pk})
        )

        self.assertContains(response, __class__.order.delivery_address)
        self.assertContains(response, __class__.order.promocode)
        response_order = response.context['order']
        self.assertEqual(response_order.pk, __class__.order.pk)


class OrdersListViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='bob_test', password='qwerty')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(response, 'Orders')

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertEquals(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixtures.json',
        'auth-fixtures.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse('shopapp:products-export'),
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by('pk').all()
        expected_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'archived': product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data['products'],
            expected_data,
        )


class OrdersExportViewTestCase(TestCase):
    fixtures = [
        'products-fixtures.json',
        'auth-fixtures.json',
        'orders-fixtures.json',
    ]

    def test_get_orders_view(self):
        response = self.client.get(
            reverse('shopapp:orders-export'),
        )
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by('pk').all()
        expected_data = [
            {
                'ID': orders.id,
                'delivery_address': orders.name,
                'promocode': orders.promocode,
                'user': orders.user,
                'products': orders.product,
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(
            orders_data['orders'],
            expected_data,
        )


