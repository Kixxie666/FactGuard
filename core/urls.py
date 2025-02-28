from django.urls import path, include
from django.contrib import admin
from core.views import home, register, user_login, user_logout, save_website, profile, classify

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("classify/", classify, name="classify"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("save-website/", save_website, name="save_website"),
]
