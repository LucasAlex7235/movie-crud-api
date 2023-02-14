from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import User
import ipdb

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class AccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data: dict):
        if User.objects.filter(email=validated_data['email']).exists():
            raise ValidationError({'email': 'email already registered.'})
        if User.objects.filter(username=validated_data['username']).exists():
            raise ValidationError({'username': 'username already taken.'})
        return User.objects.create_user(**validated_data)
