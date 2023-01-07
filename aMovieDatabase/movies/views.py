from django.shortcuts import render
from .models import Movie
from reviews.models import ReviewImage, Reviewinfo
import json
 
 
def movie(request):
    movies = Movie.objects.all()
    review_images =ReviewImage.objects.values('caption', 'image').distinct()
    context = {'movies': movies, 'review_images': review_images}
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