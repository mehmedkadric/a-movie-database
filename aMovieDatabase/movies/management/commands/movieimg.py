from movies.models import Movie, MovieImage
import requests

# Replace YOUR_API_KEY with your actual API key
api_key = '0054701133c7db286d97296dffb4f6a9'

# Get a list of all movies
movies = Movie.objects.all()

for movie in movies:
    # Get the movie's title
    title = movie.title

    # Search for movies by title
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
    response = requests.get(url)

    # Get the first movie in the list of results
    result = response.json()['results'][0]

    # Get the movie's ID
    movie_id = result['id']

    # Retrieve information about the movie
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    movie_info = response.json()

    # Get the poster image for the movie
    poster_path = movie_info['poster_path']

    # Construct the URL of the poster image
    poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
    print(poster_url)

    # Create a new MovieImage instance
    movie_image = MovieImage(movie=movie, image=poster_url, caption=title)
    movie_image.save()
