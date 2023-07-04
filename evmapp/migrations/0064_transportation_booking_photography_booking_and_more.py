# Generated by Django 4.1.5 on 2023-05-18 06:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evmapp', '0063_user_remove_catering_booking_catering_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('location', models.TextField()),
                ('travels_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.transportation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Photography_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('studio_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.photography')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('location', models.TextField()),
                ('program_service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.entertainment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Decoration_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('location', models.TextField()),
                ('decoration_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.decoration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Convention_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('convention_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.convention')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Catering_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('date', models.DateField()),
                ('message', models.TextField()),
                ('location', models.TextField()),
                ('catering_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.catering')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Accommodation_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('rooms', models.IntegerField()),
                ('date', models.DateField()),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.accommodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evmapp.user')),
            ],
        ),
    ]
