# Generated by Django 5.0.9 on 2025-01-03 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_auth', '0001_initial'),
        ('restaurant', '0001_initial'),
        ('restaurant_customer', '0001_initial'),
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='customers',
            field=models.ManyToManyField(related_name='customer_restaurants', to='restaurant_customer.restaurantcustomer'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='login_logs',
            field=models.ManyToManyField(related_name='restaurants', to='custom_auth.loginlog'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurants', to='restaurant.restaurantcategory'),
        ),
        migrations.AddField(
            model_name='restaurantemployee',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_employees', to='restaurant.restaurant'),
        ),
        migrations.AddField(
            model_name='restaurantemployee',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_employees', to='unit.unit'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='employees',
            field=models.ManyToManyField(related_name='employee_restaurants', to='restaurant.restaurantemployee'),
        ),
        migrations.AddIndex(
            model_name='restaurantemployee',
            index=models.Index(fields=['first_name', 'last_name', 'email'], name='restaurant_employee_idx'),
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['restaurant_id', 'name'], name='restaurant__id_name_idx'),
        ),
    ]