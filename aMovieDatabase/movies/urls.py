from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('movies/', views.movie, name='movie'),
    path('movies/<str:title>/', views.movie_detail, name='movie_detail'),
]