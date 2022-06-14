from django.conf import settings
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from price_predict.schema.default import ModelConstant
from keras.models import load_model
import joblib, jwt, keras as K

from .models import Product
from .serializers import (pricePredictSerializer, StockInSerializer, StockOutSerializer)
from accounts.models import UserModel

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))


class pricePredictView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.serializer = pricePredictSerializer
        self.model = load_model('./model/model_repfit_v1.h5', custom_objects={'rmse': rmse})
        self.model.load_weights('./model/model_repfit_weight_v1.h5')
    
    def get(self, request, *args, **kwargs):
        user_id = request.headers['Authorization']
        split = user_id.split(" ")
        secret_code = settings.SECRET_KEY
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        decode = jwt.decode(split[1], secret_code, algorithms=[algorithm])
        data = Product.objects.filter(user_id=decode["user_id"]).values("category", "id_product", "price", "stock")
        x = 0
        for i in data:
            x += i["stock"]
        return Response({
            "product": data,
            "all_stock": x,
            "total": len(data)
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "category": request.data['category'],
            "id_product": request.data['id_product'],
            "stock": request.data['stock'],
            "height": request.data['height'],
            "width": request.data['width'],
            "depth": request.data['depth'],
            "cost": request.data['cost'],
            "material": request.data['material']
        }
        parser = self.serializer(data=data)

        user_id = request.headers['Authorization']
        split = user_id.split(" ")
        secret_code = settings.SECRET_KEY
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        decode = jwt.decode(split[1], secret_code, algorithms=[algorithm])

        if data['cost'] <= 300000:
            return Response({"message": "Cost must be above 300K"}, status=status.HTTP_400_BAD_REQUEST)

        prov = []
        conv_to_arab = data['cost']/3900
        print(conv_to_arab)
        obj = ModelConstant.processing(data["height"], data["depth"], data["width"], conv_to_arab, data["category"], data["material"])
        conv = list(obj.values())
        prov.append(conv)

        scaler_load = joblib.load("./model/repfit_scaler.joblib")
        result_scale = scaler_load.transform(prov)
        print(result_scale)
        prediction_result = str(self.model.predict(result_scale)[0][0])
        price = (float(prediction_result) * (9585 - 10) + 10)
        conv_money = price *  3900 

        if parser.is_valid():
            Product.objects.save_product(
                decode['user_id'], data['id_product'], data['category'],data['stock'], data['height'], 
                data['width'], data['depth'], data['cost'], data['material'], conv_money
            )
            return Response({"message": "Product has been saved", "price": conv_money}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Failed: Incorrect data type entered"}, status=status.HTTP_400_BAD_REQUEST)

class getProduct(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category):
        user_id = request.headers['Authorization']
        split = user_id.split(" ")
        secret_code = settings.SECRET_KEY
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        decode = jwt.decode(split[1], secret_code, algorithms=[algorithm])
        data = Product.objects.filter(user_id=decode["user_id"]).filter(category=category).values("category", "id_product", "price", "stock")
        x = 0
        for i in data:
            x += i["stock"]
        return Response({
            "product": data,
            "all_stock": x,
            "total": len(data)
        }, status=status.HTTP_200_OK)


class StockInView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = StockInSerializer
    
    def post(self, request, *args, **kwargs):
        input_data = {
            "added_stock": request.data['added_stock'],
            "product": kwargs.get('product_id'),
        }
        
        token_jwt = request.headers['Authorization'].split(" ")[1]
        decoded_token_jwt = jwt.decode(token_jwt, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
        
        # create user object
        user_object = UserModel.objects.get(id=decoded_token_jwt["user_id"])

        serializer = self.get_serializer(data=input_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"] = user_object
        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class StockOutView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = StockOutSerializer
    
    def post(self, request, *args, **kwargs):
        input_data = {
            "removed_stock": request.data["removed_stock"],
            "your_price": request.data["your_price"],
            "date": request.data["date"],
            "product": kwargs.get("product_id"),
        }
        
        token_jwt = request.headers['Authorization'].split(" ")[1]
        decoded_token_jwt = jwt.decode(token_jwt, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT['ALGORITHM'])
        
        # create user object
        user_object = UserModel.objects.get(id=decoded_token_jwt["user_id"])
        
        serializer = self.get_serializer(data=input_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = user_object
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
