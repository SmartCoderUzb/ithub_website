from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from .models import User

def register(request):
    """User registration view (for Django templates)."""
    if request.method == 'POST':
        ism = request.POST.get('ism')
        familiya = request.POST.get('familiya')
        t_yil = request.POST.get('t_yil')
        tel = request.POST.get('tel')
        password = request.POST.get('password')

        if not all([ism, familiya, t_yil, tel, password]):
            return render(request, 'register.html', {'error': 'All fields are required'})

        if User.objects.filter(tel=tel).exists():
            return render(request, 'register.html', {'error': 'Phone number already exists'})

        user = User.objects.create_user(ism=ism, familiya=familiya, t_yil=t_yil, tel=tel, password=password)
        
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')

def login(request):
    """User login view (for Django templates)."""
    if request.method == 'POST':
        tel = request.POST.get('tel')
        password = request.POST.get('password')

        user = User.objects.filter(tel=tel).first()
        if not user or not check_password(password, user.password):
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        auth_login(request, user)
        return redirect('home')  # Redirect to home page after login

    return render(request, 'login.html')


def chiqish(request):
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def profile(request):
    return render(request, "profile.html")