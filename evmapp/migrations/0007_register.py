# Generated by Django 4.1.5 on 2023-02-15 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evmapp', '0006_delete_register_delete_registration2'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('confirmpassword', models.CharField(max_length=20)),
            ],
        ),
    ]
