# Generated by Django 5.0.9 on 2024-12-23 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_customer', '0002_remove_restaurantcustomer_reservations'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='restaurantcustomer',
            table='restaurant_customer',
        ),
    ]
