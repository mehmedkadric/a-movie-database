from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView
from .forms import NewUserForm, LoginForm
from django.contrib import messages


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def registration(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            top_genres = form.cleaned_data['top_genres']
            user.top_genres.set(top_genres)
            user.save()
            username = form.cleaned_data.get('username')
            login(request)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import views as auth_views





