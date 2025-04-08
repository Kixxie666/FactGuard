from django.urls import path, include
from django.contrib import admin
from .views import classify_news

urlpatterns = [
    path('classify/', classify_news, name="classify_news"),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
