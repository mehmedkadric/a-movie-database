from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)

def handle_404(request, exception):
    return render(request, 'handle_error.html')

def handle_500(request):
    return render(request, 'handle_error.html')

def about(request):
    return render(request, 'about.html', {'title': 'About',})
