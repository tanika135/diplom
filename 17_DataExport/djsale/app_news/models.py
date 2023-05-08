from django.db import models
from django.urls import reverse


class NewsItem(models.Model):
    title = models.CharField(max_length=128, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст записи')
    is_published = models.BooleanField(default=False)
    type = models.ForeignKey('NewsItem', on_delete=models.CASCADE, related_name='nems', null=True)
    description = models.TextField(verbose_name='описание', default='')
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-item', args=[str(self.id)])


class NewsType(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    code = models.CharField(max_length=64, verbose_name='код')

    class Meta:
        verbose_name = 'тип новостей'
        verbose_name_plural = 'типы новостей'

    def __str__(self):
        return self.name


