
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/<str:title>/', views.author_detail, name='author_detail'),
    path('reviews/<str:title>/<str:author>/', views.review_detail, name='review_detail'),



]