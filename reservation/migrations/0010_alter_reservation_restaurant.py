# Generated by Django 5.0.9 on 2024-12-04 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_auto_20241204_0105'),
        ('restaurant', '0004_alter_restaurant_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='restaurant.restaurant'),
        ),
    ]
