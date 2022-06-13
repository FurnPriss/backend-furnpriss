from django.urls import path
from .views import RegistrationViewAPI, GenerateCodeAPI, VerifyCodeAPI, updateAccount

app_name='user'

urlpatterns = [
    path('register/', RegistrationViewAPI.as_view(), name='register'),
    path('reset-psw/', GenerateCodeAPI.as_view(), name='reset'),
    path('reset-psw/confirm', VerifyCodeAPI.as_view(), name='verify'),
    path('update-psw/', updateAccount.as_view(), name='update')
]
