# Generated by Django 4.1.5 on 2023-01-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
