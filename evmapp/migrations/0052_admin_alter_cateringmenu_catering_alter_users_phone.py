# Generated by Django 4.1.5 on 2023-05-15 05:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evmapp', '0051_delete_image_alter_photos_collection_hotel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('admin_username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')])),
                ('password', models.CharField(max_length=20)),
                ('confirmpassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cateringmenu',
            name='catering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catering_menu', to='evmapp.catering'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number.')]),
        ),
    ]
