# Generated by Django 5.0.4 on 2024-04-21 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_title_tag_alter_news_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
