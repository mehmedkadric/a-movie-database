from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)