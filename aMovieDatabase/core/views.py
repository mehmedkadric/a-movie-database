from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate the form data (omitted for simplicity)

        # Create a new user instance
        User = get_user_model()
        new_user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Save the new user to the database
        new_user.save()

        # Redirect to a success page
        return redirect('home')
    else:
        # Render the form template
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')  # Store the error message in a cookie
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')