from django.urls import path
from .views import profile
from django.urls import path, include
from .views import home, register, user_login, user_logout
<<<<<<< HEAD
from . import views
=======
from django.contrib import admin
from core.views import save_website


>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)

urlpatterns = [
    path("profile/", profile, name="profile"),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
<<<<<<< HEAD
    path('classify/', views.classify, name='classify'),
=======
    path('', include('fake_news_detection.urls')),
>>>>>>> 780b8b26 (Going back to wherer i was from a different version after the revert.)
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("save-website/", save_website, name="save_website")
]


