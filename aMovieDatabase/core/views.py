from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def registration(request):
    if request.method == 'POST':
        messages.info(request, "Please login or register.")
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f"Authentication successful")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('home.html')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})
