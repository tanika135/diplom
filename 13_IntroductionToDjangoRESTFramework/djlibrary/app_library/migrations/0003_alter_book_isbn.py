# Generated by Django 4.2 on 2023-05-02 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0002_alter_author_birth_year_alter_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=200, verbose_name='isbn'),
        ),
    ]
