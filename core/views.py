from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import SavedWebsite, Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def classify(request):
    return render(request, 'core/classify.html')

def home(request):
    return render(request, "core/home.html")

@login_required
def save_website(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            # Ensure the website is saved uniquely per user
            SavedWebsite.objects.get_or_create(user=request.user, url=url)
    return redirect("home")

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Ensure profile exists

    if request.method == "POST":
        profile_picture = request.FILES.get("profile_picture")
        if profile_picture:
            profile.profile_picture = profile_picture
            profile.save()

    return render(request, "core/profile.html", {"profile": profile})
