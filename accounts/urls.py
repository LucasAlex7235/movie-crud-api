from django.urls import path
from rest_framework_simplejwt import views
from .views import AccountView, LoginJWTView, AccountViewDetail

urlpatterns = [
    path("users/", AccountView.as_view()),
    path("users/<int:user_id>/", AccountViewDetail.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
