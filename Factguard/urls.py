from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.urls import reverse
from core.views import save_website

def home(request):
    return render(request, "core/home.html")
urlpatterns = [
    path('fake-news/', include('fake_news_detection.urls')),
    path("save-website/", save_website, name="save_website"),
    path('', include('core.urls')),
]
