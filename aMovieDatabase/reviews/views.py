from django.shortcuts import render
from .models import Reviewinfo
from movies.models import MovieImage


def reviews(request):
    reviews = Reviewinfo.objects.values('title').distinct()
    movie_data = MovieImage.objects.values('caption', 'image').distinct()
    movie_image = MovieImage.objects.all().distinct()
    content = {
        'movie_data': movie_data

    }
    return render(request, 'reviews.html', {'reviews': reviews, 'movie_image': movie_image , 'content' : content})

def author_detail(request, title):
  # Get the reviews for the movie with the specified title
  movie_reviews = Reviewinfo.objects.filter(title=title)

  # Render the reviews template with the movie reviews
  return render(request, 'author_list.html', {'reviews': movie_reviews})

def review_detail(request, title, author):
    review = Reviewinfo.objects.filter(title=title, author=author).first()
    movie_image = MovieImage.objects.filter(caption=title).first()
    return render(request, 'review_detail.html', {'review': review, 'movie_image': movie_image})





