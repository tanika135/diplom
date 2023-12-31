# Generated by Django 4.2 on 2023-05-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя автора')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(related_name='posts', to='app_blogs.author'),
        ),
    ]
