# Generated by Django 5.0.4 on 2024-04-21 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('picture', models.ImageField(default='avatar.png', upload_to='pictures/')),
                ('tag', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='news.title')),
            ],
            options={
                'ordering': ('tag',),
            },
        ),
    ]
