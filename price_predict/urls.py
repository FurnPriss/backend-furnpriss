from django.urls import path
from .views import pricePredictView

app_name='pred'

urlpatterns = [
    path('predict/', pricePredictView.as_view(), name='price')
]
