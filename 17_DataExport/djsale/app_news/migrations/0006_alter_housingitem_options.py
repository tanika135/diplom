# Generated by Django 4.2 on 2023-05-09 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_alter_housingitem_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housingitem',
            options={'verbose_name': 'Жилье', 'verbose_name_plural': 'Жилье'},
        ),
    ]
