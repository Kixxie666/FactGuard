from django.shortcuts import render, redirect
from django.contrib.auth  import login, authenticate, logout
from .models import SavedWebsite
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

<<<<<<< HEAD
from django.shortcuts import render

def classify(request):
    return render(request, 'core/classify.html')
=======
def home(request):
    return render(request, "core/home.html")  # Ensure this template exists

@login_required
def save_website(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            SavedWebsite.objects.get_or_create(user=request.user, url=url)
    return redirect("home")

@login_required
def profile(request):
    if request.method == "POST":
        profile_picture = request.FILES.get("profile_picture")
        if profile_picture:
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.profile_picture = profile_picture
            profile.save()
    
    return render(request, "core/profile.html")
>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)
