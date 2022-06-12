from django.urls import path
from .views import RegistrationViewAPI, GenerateCodeAPI, VerifyCodeAPI, LogoutView

app_name='user'

urlpatterns = [
    path('register/', RegistrationViewAPI.as_view(), name='register'),
    path('reset-psw/', GenerateCodeAPI.as_view(), name='reset'),
    path('reset-psw/confirm', VerifyCodeAPI.as_view(), name='verify'),
    path('logout/', LogoutView.as_view(), name='logout')
]
