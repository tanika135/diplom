from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    surname = models.CharField(max_length=200, verbose_name='фамилия')
    birth_year = models.IntegerField(verbose_name="год рождения")


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    isbn = models.CharField(max_length=200, verbose_name='isbn')
    year = models.IntegerField(verbose_name="год выпуска")
    pages = models.IntegerField(verbose_name='количество страниц')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

