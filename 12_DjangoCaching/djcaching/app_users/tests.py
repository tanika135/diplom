from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import translation

from app_shops.models import Actions, Offers
from app_users.models import Balance
from app_users.views import get_balance, get_promotions, get_offers, get_payment_history
from orders.models import Order


class UsersViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        translation.activate('ru')
        cls.user = User.objects.create_user(username='bob_test', password='qwerty')
        cls.balance = Balance.objects.create(amount=10000, user=cls.user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()
        cls.balance.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_user_account(self):
        response = self.client.get(reverse('app_users:about-me'))
        self.assertTemplateUsed(response, 'app_users/about-me.html')
        self.assertEquals(response.context['balance'], self.balance.amount)

        self.assertQuerySetEqual(
            qs=Actions.objects.filter(created_from__lte=datetime.now(), created_to__gte=datetime.now()),
            values=[s.pk for s in response.context['promotions']],
            transform=lambda s: s.pk
        )
        self.assertQuerySetEqual(
            qs=Offers.objects.filter(active=True),
            values=[s.pk for s in response.context['offers']],
            transform=lambda s: s.pk
        )
        self.assertQuerySetEqual(
            qs=Order.objects.filter(created_by=self.user.id),
            values=[s.pk for s in response.context['payment_history']],
            transform=lambda s: s.pk
        )

    def test_get_balance(self):
        response = get_balance(self.user.id)
        self.assertEquals(response, self.balance.amount)

    def test_get_promotions(self):
        response = get_promotions()
        self.assertQuerySetEqual(
            qs=Actions.objects.filter(created_from__lte=datetime.now(), created_to__gte=datetime.now()),
            values=[s.pk for s in response],
            transform=lambda s: s.pk
        )

    def test_get_offers(self):
        response = get_offers()
        self.assertQuerySetEqual(
            qs=Offers.objects.filter(active=True),
            values=[s.pk for s in response],
            transform=lambda s: s.pk
        )

    def test_get_payment_history(self):
        response = get_payment_history(self.user.id)
        self.assertQuerySetEqual(
            qs=Order.objects.filter(created_by=self.user.id),
            values=[s.pk for s in response],
            transform=lambda s: s.pk
        )

