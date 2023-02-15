from rest_framework.views import APIView, Request, Response, status
from .serializers import CustomJWTSerializer, AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

# Create your views here.

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