from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import SavedWebsite, Profile
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator
from .models import CommunityPost, Vote

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
            SavedWebsite.objects.get_or_create(user=request.user, url=url)
    return redirect("home")

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user) 

    if request.method == "POST":
        profile_picture = request.FILES.get("profile_picture")
        if profile_picture:
            profile.profile_picture = profile_picture
            profile.save()

    return render(request, "core/profile.html", {"profile": profile})

@csrf_exempt
def post_url(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post, created = CommunityPost.objects.get_or_create(
            url=data.get('url'),
            defaults={'description': data.get('description'), 'posted_by': request.user}
        )
        return JsonResponse({"message": "Posted successfully!"}, status=201)

@csrf_exempt
def vote(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        post = get_object_or_404(CommunityPost, id=post_id)
        vote, created = Vote.objects.update_or_create(
            post=post,
            user=request.user,
            defaults={'vote_type': data.get('vote_type')}
        )

        if post.should_be_removed():
            post.delete()
            return JsonResponse({"message": "Post removed due to downvotes"}, status=200)

        return JsonResponse({"message": "Vote registered"}, status=200)

def community_board(request):
    post_list = CommunityPost.objects.all().order_by("-created_at") 
    paginator = Paginator(post_list, 5)  

    page_number = request.GET.get("page") 
    posts = paginator.get_page(page_number)  

    return render(request, "core/community_board.html", {"posts": posts})
@csrf_exempt
@login_required
def submit_for_verification(request):
    if request.method == "POST":
        data = json.loads(request.body)
        url = data.get("url")
        description = data.get("description", "User-verified news link")

        if not url:
            return JsonResponse({"message": "URL is required!"}, status=400)

        post, created = CommunityPost.objects.get_or_create(
            url=url,
            defaults={"description": description, "posted_by": request.user}
        )

        return JsonResponse({"message": "Submitted for community verification!"}, status=201)
