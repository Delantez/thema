# Generated by Django 5.0.7 on 2024-07-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microfinance', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guarantor',
            new_name='Client',
        ),
    ]
