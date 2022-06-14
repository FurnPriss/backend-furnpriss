from django.urls import path
from .views import pricePredictView, getProduct, productSaveView

app_name='pred'

urlpatterns = [
    path('predict/', pricePredictView.as_view(), name='price'),
    path('predict/save/', productSaveView.as_view(), name='save'),
    path('predict/<str:category>', getProduct.as_view(), name='details')
]
