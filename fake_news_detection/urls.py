from django.urls import path, include
from .views import classify_news

urlpatterns = [
    path('classify/', classify_news, name="classify_news"),
]
