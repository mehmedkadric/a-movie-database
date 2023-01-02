from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm,RegistrationForm


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user instance
            User = get_user_model()
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Save the new user to the database
            new_user.save()
            # Add a success message
            messages.success(request, 'Successfully registered!')
            # Redirect to a success page
            return redirect('home')
        else:
            messages.error(request, 'Error: invalid form')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')  # Store the error message in a cookie
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')