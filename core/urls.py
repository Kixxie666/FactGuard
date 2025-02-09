from django.urls import path
from .views import home, register, user_login, user_logout
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('classify/', views.classify, name='classify'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
