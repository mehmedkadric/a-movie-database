# Generated by Django 3.2.16 on 2023-01-05 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_remove_movie_reviewinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]