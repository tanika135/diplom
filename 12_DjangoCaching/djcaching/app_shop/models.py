from django.db import models


class Shop(models.Model):
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


class Product(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

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
    class Meta:
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
