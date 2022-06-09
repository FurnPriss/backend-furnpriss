from django.conf import settings
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, TokenVerifySerializer

from accounts.models import UserModel


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer, serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8, max_length=255)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data = {
            "error": False,
            "message": "The tokens has been generated successfully.",
            "data": {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }
        }

        if settings.SIMPLE_JWT['UPDATE_LAST_LOGIN']:
            update_last_login(None, self.user)

        return data

    class Meta:
        model = UserModel
        fields = ('email', 'password')


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])

        data = {
            "error": False,
            "message": "Access token regenerated successfuly.",
            "data": {
                "access_token": str(refresh.access_token)
            }
        }

        if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
            if settings.SIMPLE_JWT['BLACKLIST_AFTER_ROTATION']:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)

        return data


class CustomTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        token = UntypedToken(attrs["token"])

        return {
            "error": False,
            "message": "The token is verified and can be used.",
        }
