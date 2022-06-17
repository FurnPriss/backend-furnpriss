from django.urls import path
from .views import RegistrationViewAPI, GenerateCodeAPI,updateAccount

app_name='user'

urlpatterns = [
    path('register/', RegistrationViewAPI.as_view(), name='register'),
    path('reset-psw/', GenerateCodeAPI.as_view(), name='reset'),
    path('update-psw/', updateAccount.as_view(), name='update')
]
