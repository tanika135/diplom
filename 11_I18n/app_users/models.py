from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass

    class Meta:
        verbose_name_plural = _('users')
        verbose_name = _('user')
