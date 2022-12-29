from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)
