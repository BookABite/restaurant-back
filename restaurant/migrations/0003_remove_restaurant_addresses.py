# Generated by Django 5.0.9 on 2024-11-17 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='addresses',
        ),
    ]