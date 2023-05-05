from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


class Product(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    shops = models.ManyToManyField(Shop)

    def __str__(self) -> str:
        return f'Product(pk={self.pk}, name={self.name!r})'
