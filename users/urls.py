from django.urls import path

from .views import login, chiqish, profile


urlpatterns = [
    path('login/', login, name="login"),
    path("logout/", chiqish, name="logout"),
    path("profile/", profile, name="profile")
]