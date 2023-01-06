from django.contrib import admin
from .models import Movie, ReviewImage

class MovieAdmin(admin.ModelAdmin):
        list_display = ('budget', 'genres', 'homepage', 'movie_id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count')

class ReviewImageAdmin(admin.ModelAdmin):
        list_display = ('movie', 'image', 'caption')

admin.site.register(Movie, MovieAdmin)
admin.site.register(ReviewImage, ReviewImageAdmin)


# Register your models here.

