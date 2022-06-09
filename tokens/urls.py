from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .apps import TokensConfig
from .views import CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView
app_name = TokensConfig.name

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='verify'),
]
