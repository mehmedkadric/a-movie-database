# Generated by Django 3.2.16 on 2023-01-05 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviewinfo',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewinfo'),
        ),
    ]
