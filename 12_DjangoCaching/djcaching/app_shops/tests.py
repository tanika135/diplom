from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from app_shops.models import Product, Shop


class CachedTestCase(TestCase):
    def test_page_with_cached_fragments(self):
        translation.activate('ru')
        response = self.client.get(reverse('app_shops:page_with_cached_fragments'))
        self.assertTemplateUsed(response, 'app_shops/page_with_cached_fragments.html')
        self.assertQuerySetEqual(
            qs=Shop.objects.all(),
            values=[s.pk for s in response.context['shops']],
            transform=lambda s: s.pk
        )


class ProductsListViewTestCase(TestCase):
    def test_product_list_view(self):
        translation.activate('ru')
        response = self.client.get(reverse('app_shops:products_list'))
        self.assertTemplateUsed(response, 'app_shops/products-list.html')
        self.assertQuerySetEqual(
            qs=Product.objects.all(),
            values=[s.pk for s in response.context['products']],
            transform=lambda s: s.pk
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        translation.activate('ru')
        super().setUpClass()
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse('app_shops:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertEquals(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse('app_shops:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertContains(response, self.product.name)
