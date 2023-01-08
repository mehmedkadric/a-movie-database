from django.shortcuts import render
from .models import Movie
from reviews.models import ReviewImage,Reviewinfo
import json
 
 
def movie(request):
    movies = Movie.objects.all()
    review_images =ReviewImage.objects.values('caption', 'image').distinct()

    matching_movies = []

    for review_image in review_images:
        caption = review_image['caption']
        for movie in movies:
            if movie.title == caption:
                matching_movies.append(movie)

    # Sort the movies by vote_average in descending order
    sorted_movies = sorted(matching_movies, key=lambda x: x.vote_average, reverse=True)[:3]

    context = {'movies': movies, 'review_images': review_images,  'sorted_movies': sorted_movies}
    return render(request, 'movies.html', context)
 
 
 
def movie_detail(request, title):
    # Get the reviews for the movie with the specified title
    movie = Movie.objects.filter(title=title).values()[0]
    reviews = Reviewinfo.objects.filter(title=title)
    review_image = ReviewImage.objects.filter(caption=title).first()
    x = json.loads(movie['genres'])
    movie['genres'] = [d['name'] for d in x]
    # Render the reviews template with the movie reviews
    return render(request, 'movie_info.html', {'movie': movie, 'reviews': reviews , 'review_image':  review_image})

