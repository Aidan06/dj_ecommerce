# Generated by Django 4.2.3 on 2023-07-31 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_phone_number'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='t_users',
        ),
    ]
