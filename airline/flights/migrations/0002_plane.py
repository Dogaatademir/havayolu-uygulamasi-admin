# Generated by Django 4.2.14 on 2024-07-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('registiration_number', models.CharField(max_length=100)),
            ],
        ),
    ]
