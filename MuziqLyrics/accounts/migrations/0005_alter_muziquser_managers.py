# Generated by Django 4.2.11 on 2024-04-06 10:21

import MuziqLyrics.accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_muziquser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='muziquser',
            managers=[
                ('objects', MuziqLyrics.accounts.managers.MuziqUserManager()),
            ],
        ),
    ]
