from django.test import TestCase
from .scoring_algorithm import score_movies
from .models import Movie
from datetime import date

class ScoreMoviesTest(TestCase):
    def setUp(self):
        self.movie1 = Movie.objects.create(title='Movie 1', popularity=5, vote_average=8, budget=0, revenue = 0, runtime=0, vote_count=0, movie_id=1, release_date=date.today())
        self.movie2 = Movie.objects.create(title='Movie 2', popularity=9, vote_average=6, budget=0,  revenue = 0,   runtime=0, vote_count=0, movie_id=2, release_date=date.today())
        self.movie3 = Movie.objects.create(title='Movie 3', popularity=7, vote_average=7,budget=0, revenue = 0,  runtime=0, vote_count=0,  movie_id=3 , release_date=date.today())

    def test_score_movies(self):
        movies = [self.movie1, self.movie2, self.movie3]
        top_movies = score_movies(movies)
        self.assertEqual(len(top_movies), 3)
        self.assertEqual(top_movies[0].title, 'Movie 2')
        self.assertEqual(top_movies[1].title, 'Movie 3')
        self.assertEqual(top_movies[2].title, 'Movie 1')
