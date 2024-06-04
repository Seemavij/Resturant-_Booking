# Generated by Django 4.2.13 on 2024-06-04 09:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('number_of_guests', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('08:00 AM', '08:00 AM'), ('09:00 AM', '09:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 PM', '12:00 PM'), ('13:00 PM', '13:00 PM'), ('14:00 PM', '14:00 PM'), ('15:00 PM', '15:00 PM')], default='08:00 AM', max_length=8)),
            ],
        ),
    ]
