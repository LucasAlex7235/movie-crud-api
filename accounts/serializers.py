from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Account
import ipdb


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data: dict):
        if Account.objects.filter(email=validated_data["email"]).exists():
            raise ValidationError({"email": "email already registered."})
        elif Account.objects.filter(username=validated_data["username"]).exists():
            raise ValidationError({"username": "username already taken."})
        if validated_data["is_employee"]:
            return Account.objects.create_user(**validated_data, is_superuser=True, is_staff=True)
        return Account.objects.create_user(**validated_data)
