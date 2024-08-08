# Generated by Django 4.2.14 on 2024-07-22 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0009_alter_flight_plane'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='plane',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='registiration_number',
        ),
        migrations.AlterField(
            model_name='plane',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='plane',
            name='airline',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, to='flights.airline'),
            preserve_default=False,
        ),
    ]
