from django.db.models import Max
from .models import Movie, MovieImage

def score_movies(movies):
    topMovies = []
    matching_movies = []
    MAX_POPULARITY = Movie.objects.aggregate(max_popularity=Max('popularity'))['max_popularity']
    MAX_VOTE_AVERAGE = Movie.objects.aggregate(max_vote_average=Max('vote_average'))['max_vote_average']
    for movie in movies:
        scaled_popularity = movie.popularity / MAX_POPULARITY
        scaled_vote_average = movie.vote_average / MAX_VOTE_AVERAGE
        movie.final_score = (0.2 *  scaled_vote_average + 0.8 * (scaled_popularity * 10))
        matching_movies.append(movie)
    topMovies = sorted(matching_movies, key=lambda x: x.final_score, reverse=True)
    scaled_topMovies = topMovies[:3]
    for movie in scaled_topMovies:
        movie.scaled_final_score = (movie.final_score*10) + 1
    return scaled_topMovies
