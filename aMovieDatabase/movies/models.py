from django.db import models

class Movie(models.Model):
    budget = models.PositiveIntegerField()
    genres = models.TextField()
    homepage = models.URLField()
    movie_id = models.PositiveIntegerField(unique=True)
    keywords = models.TextField()
    original_language = models.CharField(max_length=2)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    release_date = models.DateField()
    revenue = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    spoken_languages = models.TextField()
    status = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    vote_average = models.FloatField()
    vote_count = models.PositiveIntegerField()

class MovieImage(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    image = models.URLField()
    caption = models.CharField(max_length=255)


