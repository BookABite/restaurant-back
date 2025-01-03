# Generated by Django 5.0.9 on 2024-12-25 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_customer', '0004_alter_restaurantcustomer_created_at'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='restaurantcustomer',
            name='restaurant__name_78fb79_idx',
        ),
        migrations.RemoveField(
            model_name='restaurantcustomer',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='restaurantcustomer',
            name='name',
        ),
        migrations.AddField(
            model_name='restaurantcustomer',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='restaurantcustomer',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddIndex(
            model_name='restaurantcustomer',
            index=models.Index(fields=['first_name', 'last_name', 'phone'], name='restaurant__name_78fb79_idx'),
        ),
    ]
