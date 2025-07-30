from django.db.transaction import rollback
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from appUsers.models import User


class CustomTokenObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token["username"] = user.username
        token["role"] = user.role
        return token

    def validate(self, attrs):
        print(">>> Inside validate() with:", attrs)
        data = super().validate(attrs)
        print(">>> Token data:", data)
        data["username"] = self.user.username
        data["role"] = self.user.role
        return data


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", "end_user"),
        )
        return user
