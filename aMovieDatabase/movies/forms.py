from django import forms
from .models import Movie
import json

def get_genres():
    available_genres = set()
    movies = Movie.objects.all()
    for movie in movies:
        x = json.loads(movie.genres)
        movie.genres = [d['name'] for d in x]
        available_genres.update(movie.genres)
    available_genres = sorted(list(available_genres))

    return list(zip(available_genres, available_genres))

class MovieForm(forms.ModelForm):
    image = forms.CharField(max_length=255)
    release_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-control-light', 'placeholder': 'YYYY-MM-DD'}))
    STATUS_CHOICES = (
        ('Released', 'Released'),
        ('Not released', 'Not released'),
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-control form-control-light'}))
    runtime = forms.IntegerField()
    genres = forms.MultipleChoiceField(choices=get_genres(), widget=forms.CheckboxSelectMultiple)
    title = forms.CharField(max_length=255,
                            widget=forms.TextInput(attrs={'class': 'title2'}))
    class Meta:
        model = Movie
        fields = ['title', 'genres', 'overview','runtime', 'release_date', 'status', 'image']



