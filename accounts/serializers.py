from rest_framework import serializers
from .models import UserModel, VerifyCodeModel

class UserRegistration(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=255)
    username = serializers.CharField(min_length=6, max_length=255)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')

class ResetPassword(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=8)
    confirm_password = serializers.CharField(max_length=255, min_length=8)

    class Meta:
        model = UserModel
        fields = ("email", "password", "confirm_password",)

class updateAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8)
    confirm_password = serializers.CharField(max_length=255, min_length=8)

    class Meta:
        model = UserModel
        fields = ("password", "confirm_password",)
