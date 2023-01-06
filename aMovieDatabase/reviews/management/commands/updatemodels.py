from django.core.management.base import BaseCommand
import pandas as pd
from django.db import models
from movies.models import Movie

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_csv('tmdb_5000_movies.csv')
        for index, row in df.iterrows():
            Movie.objects.create(budget=row['budget'],
                    genres=row['genres'],
                    homepage=row['homepage'],
                    movie_id=row['id'],
                    keywords=row['keywords'],
                    original_language=row['original_language'],
                    original_title=row['original_title'],
                    overview=row['overview'],
                    popularity=row['popularity'],
                    production_companies=row['production_companies'],
                    production_countries=row['production_countries'],
                    release_date=row['release_date'],
                    revenue=row['revenue'],
                    runtime=row['runtime'],
                    spoken_languages=row['spoken_languages'],
                    status=row['status'],
                    tagline=row['tagline'],
                    title=row['title'],
                    vote_average=row['vote_average'],
                    vote_count=row['vote_count'],)