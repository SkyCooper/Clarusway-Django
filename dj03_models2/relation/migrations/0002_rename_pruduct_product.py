# Generated by Django 4.1.4 on 2022-12-21 19:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pruduct',
            new_name='Product',
        ),
    ]
