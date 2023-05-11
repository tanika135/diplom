from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))


class Product(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Product(pk={self.pk}, name={self.name!r})'

    # @property
    # def stocks(self):
    #     return ShopStock.objects.filter(product=self.pk)
    # @property
    # def shops(self):
    #     shopsStock = ShopStock.objects.filter(product=self.pk)
    #     shops = [stock.shop for stock in shopsStock]
    #     return shops
