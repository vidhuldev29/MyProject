# Generated by Django 4.1.5 on 2023-05-03 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evmapp', '0046_delete_transportation'),
    ]

    operations = [
        migrations.CreateModel(
            name='transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=25)),
                ('bus', models.BooleanField(default=False)),
                ('traveller', models.BooleanField(default=False)),
                ('cars', models.BooleanField(default=False)),
                ('bus_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('traveller_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('cars_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('place', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
            ],
        ),
    ]
