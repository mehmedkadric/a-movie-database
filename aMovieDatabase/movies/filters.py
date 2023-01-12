import json
from django import forms
from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter
from .models import Movie
from django.forms.widgets import TextInput

def get_genres():
    available_genres = set()
    movies = Movie.objects.all()
    for movie in movies:
        x = json.loads(movie.genres)
        movie.genres = [d['name'] for d in x]
        available_genres.update(movie.genres)
    available_genres = list(available_genres)

    return list(zip(available_genres, available_genres))



class MovieFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    release_year_min = NumberFilter(field_name='release_date__year', lookup_expr='gte',  label='Year', widget=TextInput(attrs={'placeholder': '>='}))
    release_year_max = NumberFilter(field_name='release_date__year', lookup_expr='lte', label='', widget=TextInput(attrs={'placeholder': '<='}))
    vote_average_min = NumberFilter(field_name='vote_average', lookup_expr='gte',
                                    label='Vote average',  widget=TextInput(attrs={'placeholder': '>='}))
    vote_average_max = NumberFilter(field_name='vote_average', lookup_expr='lte',
                                    label='',  widget=TextInput(attrs={'placeholder': '<='}))
    genres = ChoiceFilter(field_name='genres', lookup_expr='contains', choices=get_genres, label='Genres', widget=forms.Select(attrs={'class': 'custom-select'}))

    class Meta:
        model = Movie
        fields = ['title', 'genres', 'release_year_min', 'release_year_max','vote_average_min','vote_average_max']


