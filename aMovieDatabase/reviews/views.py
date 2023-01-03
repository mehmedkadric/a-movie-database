from django.shortcuts import render
from .models import Reviewinfo


def reviews(request):
    reviews = Reviewinfo.objects.values('title').distinct()
    return render(request, 'reviews.html', {'reviews': reviews})

def author_detail(request, title):
  # Get the reviews for the movie with the specified title
  movie_reviews = Reviewinfo.objects.filter(title=title)

  # Render the reviews template with the movie reviews
  return render(request, 'author_list.html', {'reviews': movie_reviews})

def review_detail(request, title, author):
    review = Reviewinfo.objects.filter(title=title, author=author).first()
    return render(request, 'review_detail.html', {'review': review})






