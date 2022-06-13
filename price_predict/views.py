from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import pricePredictSerializer
from .schema import ModelConstant
import keras as K
from keras.models import load_model
from .models import Product
import joblib
import jwt

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))


class pricePredictView(APIView):
    permission_classes = [IsAuthenticated]
    

    def __init__(self):
        self.serializer = pricePredictSerializer
        self.model = load_model('./result/model_repfit_v1.h5', custom_objects={'rmse': rmse})
        self.model.load_weights('./result/model_repfit_v1_weights.h5')
    
    def get(self, request, *args, **kwargs):
        return Response({
            'error': False,
            'message': 'Now, you can predict based on the parameters you specify!!',
        })
    
    def post(self, request):
        data = {
            "id_product": request.data['id_product'],
            "stock": request.data['stock'],
            "height": request.data['height'],
            "width": request.data['width'],
            "depth": request.data['depth'],
            "cost": request.data['cost'],
            "material": request.data['material'],
            "price": request.data['price']
        }
        parser = self.serializer(data=data)

        user_id = request.headers['Authorization']
        split = user_id.split(" ")
        secret_code = settings.SECRET_KEY
        algorithm = settings.SIMPLE_JWT['ALGORITHM']
        decode = jwt.decode(split[1], secret_code, algorithms=[algorithm])

        if parser.is_valid():
            Product.objects.save_product(decode['user_id'], data['id_product'], data['stock'],data['height'], data['width'], data['depth'], data['cost'], data['material'], data['price'])
            return Response({"message": "Product has been saved"}, status=status.HTTP_201_CREATED)
        
        return Response({"message": "Failed to save product"}, status=status.HTTP_400_BAD_REQUEST)

    
    # def post(self, request):
    #     data = {
    #         'category': request.data['category'],
    #         'qty': request.data['qty'],
    #         'product_weight_g': request.data['product_weight_g'],
    #         'comp_1': request.data['comp_1'],
    #         'ps1': request.data['ps1']
    #     }
    #     parser = self.serializer(data=data)
    #     if parser.is_valid():
    #         provide = []
    #         try:
    #             obj = ModelConstant.process_data(data['category'], data['qty'], data['product_weight_g'], data['comp_1'], data['ps1'])
    #             nilai = list(obj.values())
    #         except KeyError:
    #             return Response(
    #                 {"message": "Category field must be float or number"},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )
    #         nilai = list(obj.values())
    #         provide.append(nilai)
    #         scaler_load = joblib.load("./result/scaler_v2.save")
    #         hasil_scale = scaler_load.transform(provide)
    #         prediction_result = str(self.model.predict(hasil_scale)[0][0])
    #         return Response(
    #             {
    #                 "message": "The model was successfully loaded as predict",
    #                 "unit_price": (float(prediction_result) * (364.900000 - 19.900000) + 19.900000)
    #             }, status=status.HTTP_200_OK
    #         )
    #     return Response(parser.errors, status=status.HTTP_400_BAD_REQUEST)
