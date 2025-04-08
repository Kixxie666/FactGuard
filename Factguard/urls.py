from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core.views import save_website

def home_redirect(request):
    return redirect('classify_news')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path('fake-news/', include('fake_news_detection.urls')),
    path("save-website/", save_website, name="save_website"),  
]
