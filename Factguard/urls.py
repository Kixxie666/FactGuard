from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.urls import reverse
from core.views import save_website

def home_redirect(request):
    return redirect(reverse('classify_news'))
urlpatterns = [
    path('fake-news/', include('fake_news_detection.urls')),
    path("save-website/", save_website, name="save_website"),  
]
