# Generated by Django 4.2 on 2023-05-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop',
        ),
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(to='app_shop.shop'),
        ),
    ]