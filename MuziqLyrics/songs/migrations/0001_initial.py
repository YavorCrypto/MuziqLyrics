# Generated by Django 4.2.11 on 2024-03-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lyrics', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(choices=[('Classical', 'Classical'), ('Jazz', 'Jazz'), ('Rock', 'Rock'), ('Pop', 'Pop'), ('Hip Hop', 'Hip Hop'), ('Country', 'Country'), ('Electronic', 'Electronic')], max_length=20)),
                ('artists', models.ManyToManyField(to='artists.artist')),
            ],
        ),
    ]
