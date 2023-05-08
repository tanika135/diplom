from django.contrib.auth.models import User
from django.db import models

from orders.models import Order, OrderItem
import logging


logger = logging.getLogger(__name__)


class Balance(models.Model):
    amount = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(models.Model):
    class Meta:
        ordering = ['user']

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def status(self):
        result = 0
        orders = Order.objects.filter(created_by=self.user)
        for order in orders:
            items = OrderItem.objects.filter(order=order)
            result += sum([item.price*item.quantity for item in items])

        if result > 10000:
            logger.info('Переход пользователя по статусной системе')
            status = 'Platin'
        elif result > 2000:
            logger.info('Переход пользователя по статусной системе')
            status = 'Gold'
        else:
            status = 'Silver'

        return status




