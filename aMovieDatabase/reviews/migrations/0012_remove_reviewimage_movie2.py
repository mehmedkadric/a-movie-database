# Generated by Django 3.2.16 on 2023-01-07 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_reviewimage_movie2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewimage',
            name='movie2',
        ),
    ]
