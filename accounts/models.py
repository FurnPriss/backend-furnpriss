from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models
import nanoid
from rest_framework_simplejwt.tokens import RefreshToken
from manager import UserManager, VerifyCodeManager, generators


# Create your models here.
class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, default=generators.get_default_id, editable=False, max_length=32)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        text = self.email if self.email != '' else self.username
        return f"{text}"


class VerifyCodeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users_id')
    code = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    code_used = models.CharField(max_length=100)

    objects= VerifyCodeManager()

    def __str__(self):
        return "Code now has been created"
