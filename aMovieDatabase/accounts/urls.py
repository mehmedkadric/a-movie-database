from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.user_detail, name='user_detail'),
    path('register/', views.registration, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]