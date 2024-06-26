# Generated by Django 4.2.11 on 2024-04-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('artists', models.ManyToManyField(to='artists.artist')),
            ],
        ),
    ]
