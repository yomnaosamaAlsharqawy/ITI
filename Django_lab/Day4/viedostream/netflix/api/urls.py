from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import index, CreateMovie, ListMovies, api_signup, MovieViewSet

urlpatterns = [
    path("login/", obtain_auth_token),
    path("signup", api_signup),
    path('index', index, name='index'),
    path("store/", CreateMovie.as_view()),
    path("list/", ListMovies.as_view()),
    path("", MovieViewSet),
]
