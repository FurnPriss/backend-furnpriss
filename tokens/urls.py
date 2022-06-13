from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from .apps import TokensConfig
from .views import (
    CustomTokenBlacklistView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)
app_name = TokensConfig.name

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='obtain_pair'),
    path('token/blacklist', CustomTokenBlacklistView.as_view(), name='blacklist'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='verify'),
]
