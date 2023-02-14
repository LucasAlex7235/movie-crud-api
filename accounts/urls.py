from django.urls import path
from rest_framework_simplejwt import views 
from .views import AccountView, LoginJWTView

urlpatterns = [
    path("account/", AccountView.as_view()),
    path("login/", LoginJWTView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
