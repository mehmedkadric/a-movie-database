# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,User



class Genre(models.Model):
    name = models.CharField(max_length=100)

def create_genres():
    genres = ['Action', 'Comedy', 'Drama', 'Romance', 'Thriller', 'Sci-Fi', 'Adventure', 'Fantasy', 'Horror', 'Mystery', 'Anime', 'Classic', 'Western']
    for genre in genres:
        Genre.objects.get_or_create(name=genre)

create_genres()

class User(User):
    date_of_birth = models.DateField(null=True, blank=True)
    top_genres = models.ManyToManyField(Genre)