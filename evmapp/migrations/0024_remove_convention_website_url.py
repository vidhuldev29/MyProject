# Generated by Django 4.1.5 on 2023-04-18 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evmapp', '0023_convention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convention',
            name='website_url',
        ),
    ]
