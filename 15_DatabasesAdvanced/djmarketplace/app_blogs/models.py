from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

        def __str__(self):
            return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя автора')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст поста')
    is_published = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='posts')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='лайки')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title



