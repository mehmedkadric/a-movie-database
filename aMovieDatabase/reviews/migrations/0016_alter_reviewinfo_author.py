# Generated by Django 4.1.5 on 2023-01-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_remove_reviewinfo_has_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewinfo',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
