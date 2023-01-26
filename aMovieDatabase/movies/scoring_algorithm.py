from django.db.models import Max
from .models import Movie, MovieImage

def score_movies(movies):
    # Initialize an empty list to store the top movies
    topMovies = []
    # Initialize a list to store all matching movies
    matching_movies = []
    # Get the maximum popularity and vote average of all movies in the database
    max_popularity = Movie.objects.aggregate(max_popularity=Max('popularity'))['max_popularity']
    max_vote_average = Movie.objects.aggregate(max_vote_average=Max('vote_average'))['max_vote_average']
    # Iterate through the list of input movies
    for movie in movies:
        # Normalize the popularity and vote average values of each movie
        scaled_popularity = movie.popularity / max_popularity
        scaled_vote_average = movie.vote_average / max_vote_average
        # Calculate a final score for each movie
        movie.final_score = (0.2 *  scaled_vote_average + 0.8 * (scaled_popularity * 10))
        # Append each movie to the matching_movies list
        matching_movies.append(movie)
    # Sort the matching_movies list by final_score in descending order
    topMovies = sorted(matching_movies, key=lambda x: x.final_score, reverse=True)
    # Get the top 3 movies
    scaled_topMovies = topMovies[:3]
    for movie in scaled_topMovies:
        # scale the final_score and return as scaled_final_score
        movie.scaled_final_score = (movie.final_score*10) + 1
    # Return the top 3 movies
    return scaled_topMovies
