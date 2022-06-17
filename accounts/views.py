from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import UserRegistration, UserModel, ResetPassword, updateAccountSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth.hashers import make_password
from datetime import *
from django.conf import settings
import re, os, jwt, shortuuid

# Create your views here.
class RegistrationViewAPI(APIView):
    serializer_class = UserRegistration

    def __init__(self):
        self.serializer = UserRegistration
    
    def post(self, request):
        data = {
            "username": request.data['username'],
            "email": request.data['email'],
            "password": request.data['password']
        }

        serializer = self.serializer(data=data)
        pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'

        if serializer.is_valid():
            regex = re.fullmatch(pattern, data["email"])
            if not regex:
                return Response({"email": "Email must have a pattern '.com'"},status=status.HTTP_400_BAD_REQUEST)

            UserModel.objects.create_superuser(data["username"], data["email"], data["password"])

            return Response({
                "username": serializer.data["username"]
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class updateAccount(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.serializer = updateAccountSerializer

    def put(self, request):
        user_id = request.headers['Authorization']
        split = user_id.split(" ")
        secret_code = settings.SECRET_KEY
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        decode = jwt.decode(split[1], secret_code, algorithms=[algorithm])

        data = {"password": request.data["password"], "confirm_password": request.data["confirm_password"]}
        parser = self.serializer(data=data)

        query = get_object_or_404(UserModel,id=decode['user_id'])

        if data["password"] != data["confirm_password"]:
            return Response({"message": "Please correct, password and confirm password must be same"},status=status.HTTP_404_NOT_FOUND)

        if parser.is_valid():
            query.password = make_password(data["password"])
            query.save()
            return Response({"message": "Password has been updated"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Password failed to update"}, status=status.HTTP_400_BAD_REQUEST)

    
class GenerateCodeAPI(APIView):
    serializer_class = ResetPassword
    
    def __init__(self):
        self.reset = ResetPassword

    def post(self, request):
        random = shortuuid.ShortUUID().random(length=5)

        data = {
            "email": request.data["email"],
            "password": request.data["password"],
            "confirm_password": request.data["confirm_password"]
        }

        retrive = self.reset(data=data)

        if retrive.is_valid():
            exist_email = UserModel.objects.filter(email=retrive.data["email"]).exists()
            choice_email = get_object_or_404(UserModel, email=retrive.data["email"])

            if retrive.data["password"] != retrive.data["confirm_password"]:
                return Response({"message": "Please correct, password and confirm password must be same"},status=status.HTTP_404_NOT_FOUND)

            if exist_email:
                choice_email.password = make_password(retrive.data['password'])
                choice_email.save()
                response= Response({"message": "Password has been updated"}, status=status.HTTP_201_CREATED)
                return response
            else:
                return Response(
                    {
                        "message": "Email isn't available on our database"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        return Response(retrive.errors, status=status.HTTP_400_BAD_REQUEST)