# Generated by Django 4.2 on 2023-05-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0002_author_post_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='лайки'),
        ),
    ]
