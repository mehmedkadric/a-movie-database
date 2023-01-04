


import requests

# Replace YOUR_API_KEY with your actual API key
api_key = '0054701133c7db286d97296dffb4f6a9'

# Search for movies by title
title = 'Avatar'
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

# Print the URL of the poster image
print(poster_url)
