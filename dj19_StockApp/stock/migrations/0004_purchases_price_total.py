# Generated by Django 4.1.5 on 2023-01-31 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_sales_price_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=1111, max_digits=7, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]