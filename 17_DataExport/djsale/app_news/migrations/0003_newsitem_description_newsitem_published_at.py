# Generated by Django 4.2 on 2023-05-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_newstype_newsitem_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='description',
            field=models.TextField(default='', verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='published_at',
            field=models.DateTimeField(null=True, verbose_name='дата публикации'),
        ),
    ]