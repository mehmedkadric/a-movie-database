from django.shortcuts import render, redirect
from .models import Movie, MovieImage,Watchlist, Rating
from reviews.models import Reviewinfo
from reviews.forms import ReviewForm
import json, time, datetime
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.contrib import messages
from .filters import MovieFilter
from django.contrib.auth.decorators import login_required
from .forms import MovieForm

@login_required
def movie(request):
    movie_image = MovieImage.objects.values('caption', 'image').distinct()
    filter = MovieFilter(request.GET, queryset=Movie.objects.exclude(title__regex=r'^\d+').order_by('title'))
    movies = filter.qs
    topMovies = filter.qs.order_by('-vote_average')[:3]
    matching_movies = []
    for movie_image1 in movie_image:
        caption = movie_image1['caption']
        for movie in topMovies:
            if movie.title == caption:
                matching_movies.append(movie)
    if request.GET:  # check if any filters have been applied
        movies = movies.order_by('-vote_average')
    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    sorted_movies = sorted(matching_movies, key=lambda x: x.vote_average, reverse=True)[:3]
    context = {
            'movies': movies,
            'movie_image': movie_image,
            'topMovies' : topMovies,
            'sorted_movies': sorted_movies,
            'filter': filter,
            'query_params': query_params
        }
    return render(request, 'movies.html', context)




@login_required
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
                messages.success(request, 'Your review has been saved!')
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
        elif 'remove_review' in request.POST:
            # Remove the review from the database
            Reviewinfo.objects.filter(title=title, author=request.user.username).delete()
            # Redirect to the same page to show the updated list of reviews
            messages.error(request, 'Your review has been deleted!')
            return redirect('movie_detail', title=title)
        elif 'edit_review' in request.POST:
            content = request.POST.get('content')
            author = request.POST.get('author')
            review = Reviewinfo.objects.get(title=title, author=request.user.username)
            review.content = content
            review.save()
            return redirect('movie_detail', title=title)
    return render(request, 'movie_info.html',
                  {'movie': movie, 'reviews': reviews, 'movie_image': movie_image, 'form': form, 'title': title,
                   'watchlist_titles': watchlist_titles, 'user_has_submitted_review': user_has_submitted_review,
                   'formatted_runtime': formatted_runtime, 'user_rating': user_rating})

@login_required
def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    movies = Movie.objects.all()
    movie_image = MovieImage.objects.values('caption', 'image').distinct()
    movies = Movie.objects.all()
    ratings = Rating.objects.filter(username=request.user)
    rated_movies = []
    for watchlist_item in watchlist:
        for rating in ratings:
            if rating.title == watchlist_item.movie and watchlist_item.movie not in rated_movies:
                rated_movies.append(watchlist_item.movie)
                watchlist_item.movie_rating = rating.rating
                break
        if watchlist_item.movie not in rated_movies:
            watchlist_item.movie_rating = "No rating"

    context = {
        'watchlist': watchlist,
        'movie_image': movie_image,
        'ratings': ratings,
        'movies': movies
    }
    return render(request, 'watchlist.html', context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            try:
                genres = json.dumps([{"id": 0, "name": g} for g in form.cleaned_data["genres"]])
            except json.decoder.JSONDecodeError:
                genres = form.cleaned_data['genres']
                # here you can format the genres field as per your needs.
                genres = [{"id": 0, "name": genres}]
                genres = json.dumps(genres)

            movie = Movie.objects.create(
                movie_id = Movie.objects.count() + 1,
                budget = 0,
                homepage = '',
                genres = genres,
                keywords = '[{"id": 0, "name": ""}]',
                original_language = '',
                original_title = '',
                overview = form.cleaned_data['overview'],
                popularity = 0,
                production_companies = '[{"id": 0, "name": ""}]',
                production_countries = '[{"id": 0, "name": ""}]',
                release_date = form.cleaned_data['release_date'],
                revenue = 0,
                runtime = form.cleaned_data['runtime'],
                spoken_languages  = '[{"id": 0, "name": ""}]',
                status = form.cleaned_data['status'],
                tagline = '',
                title = form.cleaned_data['title'],
                vote_average = 0,
                vote_count = 0
            )
            movie_image = MovieImage.objects.create(
                movie=movie,
                image=form.cleaned_data['image'],
                caption=form.cleaned_data['title'],
            )
            messages.success(request, 'Movie has been added to DB.')
            return redirect('home')
    else:
        messages.error(request, 'There was error adding your movie.')
        form = MovieForm()

    return render(request, 'add_movie.html', {'form': form})

