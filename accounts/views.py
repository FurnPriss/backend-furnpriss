from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import UserRegistration, UserModel, ResetPassword, VerifyCodeModel, CodeVerify, updateAccountSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from dotenv import load_dotenv
from datetime import *
from django.conf import settings
import re, os, jwt, shortuuid

load_dotenv(dotenv_path='./.env')
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
        age = 365*24*60*60
        subject = "Reset Password"
        msg = f"Don't publish your verification code whatever the reason\nYour verify code: {random}"

        data = {
            "email": request.data["email"],
            "password": request.data["password"],
            "confirm_password": request.data["confirm_password"]
        }

        retrive = self.reset(data=data)
        exist_email = UserModel.objects.filter(email=data["email"]).exists()
        choice_email = get_object_or_404(UserModel, email=data["email"])

        if data["password"] != data["confirm_password"]:
            return Response({"message": "Please correct, password and confirm password must be same"},status=status.HTTP_404_NOT_FOUND)

        if retrive.is_valid():

            if exist_email:
                VerifyCodeModel.objects.create_code(user_id=choice_email.id, code=random)
                send_mail(subject, msg, os.getenv("EMAIL"),[choice_email.email], fail_silently=False)
                response= Response({"message": "We sent email to you. Please check your inbox"}, status=status.HTTP_201_CREATED)
                response.set_cookie(key="password", value=data["password"], httponly=False, expires=datetime.now() + timedelta(seconds=age), max_age=age)
                return response
            else:
                return Response(
                    {
                        "message": "Email isn't available on our database"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        return Response(retrive.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyCodeAPI(APIView):
    serializer_class = CodeVerify
    
    def __init__(self):
        self.verify = CodeVerify

    def post(self, request):
        new_password = request.COOKIES["password"]

        data = {
            "code" : request.data["code"]
        }

        check = VerifyCodeModel.objects.filter(code=data["code"]).exists()
        userid_out = get_object_or_404(VerifyCodeModel, code=data["code"])
        query = get_object_or_404(UserModel,id=userid_out.user_id)
        parser = self.verify(data=data)

        if parser.is_valid():
            if check and query:
                query.password = make_password(new_password)
                query.save()
                response = Response(status=status.HTTP_201_CREATED)
                response.delete_cookie('password')
                return response
            else:
                return Response({"message": "Code is incorrect"}, status=status.HTTP_404_NOT_FOUND)

        return Response(parser.errors, status=status.HTTP_400_BAD_REQUEST)
