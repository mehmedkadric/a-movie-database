# Generated by Django 3.2.16 on 2023-01-05 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_reviewimage'),
        ('reviews', '0010_auto_20230105_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewimage',
            name='movie2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
            preserve_default=False,
        ),
    ]
