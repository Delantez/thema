# Generated by Django 5.0.7 on 2024-07-26 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microfinance', '0006_guarantor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guarantor',
            name='phone3',
        ),
    ]
