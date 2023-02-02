# Generated by Django 4.1.5 on 2023-01-31 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_purchases_price_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]