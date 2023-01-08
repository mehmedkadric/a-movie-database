from django.shortcuts import render, redirect
from .models import Movie, MovieImage,Watchlist
from reviews.models import Reviewinfo
from reviews.forms import ReviewForm
import json
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
 
def movie(request):
    movies = Movie.objects.exclude(title__regex=r'^\d+').order_by('title')

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

    watchlist_titles = [watchlist.movie for watchlist in Watchlist.objects.filter(user=request.user)]

    username = request.user.username
    # Create the form with the title and username as arguments
    form = ReviewForm(title=title, username=username)

    if request.method == 'POST':
        # Bind the form to the POST data
        form = ReviewForm(request.POST, title=title)
        if form.is_valid():
            # Save the form data to the database
            review = form.save(commit=False)
            review.title = title
            review.save()
            # Redirect to the same page to show the updated list of reviews
            return redirect('movie_detail', title=title)
        if 'watchlist_add' in request.POST:
            # Create a new Watchlist object with the movie title and user field set to the current movie title and logged-in user, respectively
            Watchlist.objects.create(movie=title, user=request.user)
            # Redirect to the same page to show the updated watchlist
            return redirect('movie_detail', title=title)
        elif 'watchlist_remove' in request.POST:
            # Remove the movie from the user's watchlist
            Watchlist.objects.filter(movie=title, user=request.user).delete()
            # Redirect to the same page to show the updated watchlist
            return redirect('movie_detail', title=title)

    # Render the reviews template with the movie reviews
    return render(request, 'movie_info.html', {'movie': movie, 'reviews': reviews , 'movie_image':  movie_image, 'form': form,'title': title, 'watchlist_titles': watchlist_titles})
