from django.contrib.auth.models import User
from django.db import models


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Balance(models.Model):
    amount = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(models.Model):
    class Meta:
        ordering = ['user']

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def status(self):
        #result = History.objects.filter(user=self.user)#.aggregate(total=Sum(F))
        result = 20000
        if result > 50000:
            status = 'Платиновый'
        elif result > 10000:
            status = 'Золотой'
        else:
            status = 'Серебряный'

        return status




