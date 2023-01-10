from django.shortcuts import render, redirect
from .models import Movie, MovieImage,Watchlist, Rating
from reviews.models import Reviewinfo
from reviews.forms import ReviewForm
import json, time
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.contrib import messages


def movie(request):
    # Get the genre from the request
    genre = request.GET.get('genre')
    movie_image = MovieImage.objects.values('caption', 'image').distinct()
    vote_average_min = request.GET.get('vote_average_min')
    vote_average_max = request.GET.get('vote_average_max')
    titleofRequest = request.GET.get('title')
    # Get a queryset of all the movies
    movies = Movie.objects.exclude(title__regex=r'^\d+').order_by('title')

    
    matching_movies = []

    for movie_image1 in movie_image:
        caption = movie_image1['caption']
        for movie in movies:
            if movie.title == caption:
                matching_movies.append(movie)

    # Flatten the list of genres for each movie, and get the unique values
    available_genres = set()
    for movie in movies:
        x = json.loads(movie.genres)
        movie.genres = [d['name'] for d in x]
        available_genres.update(movie.genres)
    available_genres = list(available_genres)


    if vote_average_min and vote_average_max:
        movies = movies.filter(vote_average__gte=vote_average_min, vote_average__lte=vote_average_max)

    # Filter the movies queryset by the genre
    if genre:
        movies = movies.filter(genres__contains=genre)

    if titleofRequest:
        movies = movies.filter(title__icontains=titleofRequest)

    years = Movie.objects.dates('release_date', 'year', order='ASC').distinct()
    year = request.GET.get('year')
    if year:
        movies = movies.filter(release_date__year=year)
    paginator = Paginator(movies, 12)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    

    # Sort the movies by vote_average in descending order
    sorted_movies = sorted(matching_movies, key=lambda x: x.vote_average, reverse=True)[:3]
    context = {
        'movies': movies,
        'movie_image': movie_image,
        'years': years,
        'selected_year': year,
        'available_genres': available_genres,
        'genre': genre,
        'sorted_movies': sorted_movies,
        'vote_average_min': vote_average_min,
        'vote_average_max': vote_average_max,
        'titleofRequest': titleofRequest,
    }
    return render(request, 'movies.html', context)


def movie_detail(request, title):
    # Get the reviews for the movie with the specified title
    movie = Movie.objects.filter(title=title).values()[0]
    reviews = Reviewinfo.objects.filter(title=title)
    movie_image = MovieImage.objects.filter(caption=title).first()
    x = json.loads(movie['genres'])
    movie['genres'] = [d['name'] for d in x]
    hours = movie['runtime'] // 60
    minutes = movie['runtime'] % 60
    formatted_runtime = f"{hours} hours {minutes} minutes"
    user_has_submitted_review = Reviewinfo.objects.filter(title=title, author=request.user.username).exists()
    try:
        watchlist_titles = [watchlist.movie for watchlist in Watchlist.objects.filter(user=request.user)]
        user_rating = Rating.objects.filter(username=request.user.username, title=title).first()
    except TypeError:
        # redirect the user to the home page
        messages.error(request, 'You must be logged in to use these perks!')
        return redirect('home')
    username = request.user.username
    # Create the form with the title and username as arguments
    form = ReviewForm(title=title, username=username)

    if request.method == 'POST':
        # Bind the form to the POST data
        form = ReviewForm(request.POST, title=title)
        if form.is_valid():
            if not user_has_submitted_review:
                # Save the form data to the database
                review = form.save(commit=False)
                review.title = title
                review.author = request.user.username
                review.save()
                # Redirect to the same page to show the updated list of reviews
                return redirect('movie_detail', title=title)
            else:
                # Display an error message if the user has already submitted a review
                messages.error(request, 'You have already submitted a review for this movie!')
                pass
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
        # Handle the rating submission
        if 'rating' in request.POST:
            try:
                rating = Rating.objects.get(username=request.user.username, title=title)
                rating.rating = request.POST['rating']
                rating.save()
                messages.success(request,'Your rating has been saved!')
                return redirect('movie_detail', title=title)
            except Rating.DoesNotExist:
                Rating.objects.create(username=request.user.username, title=title, rating=request.POST['rating'])
                return redirect('movie_detail', title=title)
    return render(request, 'movie_info.html',
                  {'movie': movie, 'reviews': reviews, 'movie_image': movie_image, 'form': form, 'title': title,
                   'watchlist_titles': watchlist_titles, 'user_has_submitted_review': user_has_submitted_review,
                   'formatted_runtime': formatted_runtime, 'user_rating': user_rating})




