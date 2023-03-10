# Generated by Django 3.2.16 on 2023-01-05 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_reviewimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.PositiveIntegerField()),
                ('genres', models.TextField()),
                ('homepage', models.URLField()),
                ('movie_id', models.PositiveIntegerField(unique=True)),
                ('keywords', models.TextField()),
                ('original_language', models.CharField(max_length=2)),
                ('original_title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('production_companies', models.TextField()),
                ('production_countries', models.TextField()),
                ('release_date', models.DateField()),
                ('revenue', models.PositiveIntegerField()),
                ('runtime', models.PositiveIntegerField()),
                ('spoken_languages', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.PositiveIntegerField()),
                ('reviewinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewinfo')),
            ],
        ),
    ]
