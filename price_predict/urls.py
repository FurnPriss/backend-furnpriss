from django.urls import path
from .views import getProduct, pricePredictView, productSaveView, StockInView, StockOutView

app_name='pred'

urlpatterns = [
    path('predict/', pricePredictView.as_view(), name='price'),
    path('predict/save/', productSaveView.as_view(), name='save'),
    path('predict/<str:category>', getProduct.as_view(), name='details'),
    path('products/<str:product_id>/stockin', StockInView.as_view(), name='stockin'),
    path('products/<str:product_id>/stockout', StockOutView.as_view(), name='stockout'),
]
