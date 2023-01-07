from django.shortcuts import render
from .models import Movie, MovieImage
from reviews.models import Reviewinfo
import json
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
 
def movie(request):
    movies = Movie.objects.all()
    movie_image = MovieImage.objects.values('caption', 'image').distinct()

    paginator = Paginator(movies, 12)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    context = {'movies': movies, 'movie_image': movie_image}
    return render(request, 'movies.html', context)

 
 
 
def movie_detail(request, title):
    # Get the reviews for the movie with the specified title
    movie = Movie.objects.filter(title=title).values()[0]
    reviews = Reviewinfo.objects.filter(title=title)
    movie_image = MovieImage.objects.filter(caption=title).first()
    x = json.loads(movie['genres'])
    movie['genres'] = [d['name'] for d in x]
    # Render the reviews template with the movie reviews
    return render(request, 'movie_info.html', {'movie': movie, 'reviews': reviews , 'movie_image':  movie_image})