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
    is_superuser = serializers.BooleanField(read_only=True)
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data: dict):
        email_exist = Account.objects.filter(email=validated_data["email"]).exists()
        username_exist = Account.objects.filter(
            username=validated_data["username"]
        ).exists()
        email_and_username_exist = email_exist and username_exist

        if email_and_username_exist:
            raise ValidationError(
                {
                    "email": ["email already registered."],
                    "username": ["username already taken."],
                }
            )
        if email_exist:
            raise ValidationError({"email": "email already registered."})
        elif username_exist:
            raise ValidationError({"username": "username already taken."})
        if validated_data["is_employee"]:
            return Account.objects.create_user(
                **validated_data, is_superuser=True, is_staff=True
            )
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict):
        try:
            password = validated_data.pop("password")
            instance.set_password(password)
        except KeyError:
            pass
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
