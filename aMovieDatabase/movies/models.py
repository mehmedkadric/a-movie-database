from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Watchlist(models.Model):
    movie = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rating(models.Model):
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    rating = models.IntegerField()

@receiver(post_save, sender=Rating)
def update_vote_average(sender, instance, **kwargs):
    movie = Movie.objects.get(title=instance.title)
    ratings = Rating.objects.filter(title=instance.title)
    vote_average = sum([r.rating for r in ratings]) / len(ratings)
    movie.vote_average = vote_average
    movie.save()

