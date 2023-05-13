from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from app_users.models import Balance


class OrderViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='bob_test', password='qwerty')
        cls.balance = Balance.objects.create(amount=10000, user=cls.user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()
        cls.balance.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_order_create(self):
        response = self.client.get(reverse('orders:order_create'))
        self.assertTemplateUsed(response, 'orders/order/create.html')

        response = self.client.post(
            reverse('orders:order_create'),
            {
                'address': 'test address',
                'city': 'test city',
                'created_by': self.user.id
            }
        )

        self.assertTemplateUsed(response, 'orders/order/created.html')

