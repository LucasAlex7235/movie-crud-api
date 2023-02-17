from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .serializers import CustomJWTSerializer, AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwnerOrAdmin
from rest_framework import serializers
from .models import Account


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class AccountView(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except serializers.ValidationError as error:
            return Response(error.detail, status.HTTP_400_BAD_REQUEST)


class AccountViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrAdmin]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(Account, id=user_id)
        self.check_object_permissions(request, user)
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    def patch(self, request: Request, user_id) -> Response:
        import ipdb

        user = get_object_or_404(Account, id=user_id)
        self.check_object_permissions(request, user)
        serializer = AccountSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
