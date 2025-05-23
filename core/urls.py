from django.urls import path, include
from django.contrib import admin
from . import views
from .views import post_url, vote, community_board, home, register, user_login, user_logout, save_website, profile, classify, submit_for_verification, get_trending_alert
urlpatterns = [
    path("profile/", profile, name="profile"),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("classify/", classify, name="classify"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("save-website/", save_website, name="save_website"),
    path("post-url/", post_url, name="post_url"),
    path("vote/<int:post_id>/", vote, name="vote"),
    path("community-board/", community_board, name="community_board"),
    path("submit-for-verification/", submit_for_verification, name="submit_for_verification"),
    path('api/community-posts/', views.community_posts_api, name='community-posts-api'),
    path('api/submit-vote/', views.submit_vote, name='submit-vote-api'),
    path("get-trending-alert/", get_trending_alert, name="get_trending_alert"),
]
