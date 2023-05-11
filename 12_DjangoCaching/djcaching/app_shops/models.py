from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Product(pk={self.pk}, name={self.name!r})'

    @property
    def stocks(self):
        return ShopStock.objects.filter(product=self.pk)

    @property
    def shops(self):
        shopsStock = ShopStock.objects.filter(product=self.pk)
        shops = [stock.shop for stock in shopsStock]
        return shops


class ShopStock(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)


class Actions (models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    created_from = models.DateTimeField(null=False)
    created_to = models.DateTimeField(null=False)
    products = models.ManyToManyField(Product)
