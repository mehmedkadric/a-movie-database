# Generated by Django 3.2.16 on 2023-01-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimage',
            name='image',
            field=models.URLField(),
        ),
    ]
