from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('movies/', views.movie, name='movie'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('movies/details/<str:title>/', views.movie_detail, name='movie_detail'),
]