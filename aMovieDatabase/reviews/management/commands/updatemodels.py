from reviews.models import Reviewinfo, ReviewImage
import requests
from django.core.files import File
from io import BytesIO

# Replace YOUR_API_KEY with your actual API key
api_key = 'API'

# Get a list of all reviewinfos
reviewinfos = Reviewinfo.objects.all()

for reviewinfo in reviewinfos:
    # Search for movies by title
    title = reviewinfo.title
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
    response = requests.get(url)

    # Get the first movie in the list of results
    movie = response.json()['results'][0]

    # Get the movie's ID
    movie_id = movie['id']

    # Retrieve information about the movie
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    movie_info = response.json()

    # Get the poster image for the movie
    poster_path = movie_info['poster_path']

    # Construct the URL of the poster image
    poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
    print(poster_url)

    # Save the URL of the poster image to the ReviewImage model
    review_image = ReviewImage(movie=reviewinfo, image=poster_url, caption=title)
    review_image.save()
