# Generated by Django 5.1.3 on 2024-12-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_name', models.CharField(max_length=100)),
                ('about_descr', models.TextField()),
                ('about_image', models.FileField(upload_to='author_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Владелец сайта',
                'verbose_name_plural': 'Владельцы сайта',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=100)),
                ('news_short_description', models.TextField()),
                ('news_full_description', models.TextField()),
                ('news_image', models.FileField(upload_to='news_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_description', models.TextField()),
                ('category_image', models.FileField(upload_to='news_images')),
                ('category_news_num', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
    ]
