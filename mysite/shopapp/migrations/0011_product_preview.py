# Generated by Django 4.1.7 on 2023-04-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_order_reciept'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='product_preview_directory_path'),
        ),
    ]
