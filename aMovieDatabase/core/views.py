from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


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

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f'New message from {name}',
            message,
            email,
            ['kosharun04@gmail.com'],
            fail_silently=False,
        )
        return redirect('contact')
    return render(request, 'contact.html')