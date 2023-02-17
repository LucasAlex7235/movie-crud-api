from django.urls import path
from .views import MovieView, MovieViewDetail, MovieOrderView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieViewDetail.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
