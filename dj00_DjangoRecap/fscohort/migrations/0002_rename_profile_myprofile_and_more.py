# Generated by Django 4.1.6 on 2023-02-09 21:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='MyProfile',
        ),
        migrations.RenameField(
            model_name='myprofile',
            old_name='user',
            new_name='myuser',
        ),
    ]
