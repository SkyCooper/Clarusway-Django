# Generated by Django 4.1.5 on 2023-01-14 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('framework', models.ManyToManyField(db_table='dd', to='frameworkrelations.frameworks')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='frameworkrelations.creator')),
            ],
        ),
        migrations.AddField(
            model_name='frameworks',
            name='languages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frameworkrelations.languages'),
        ),
    ]
