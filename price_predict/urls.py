from django.urls import path
from .views import getProduct, pricePredictView, StockInView, StockOutView, graphStockout

app_name='pred'

urlpatterns = [
    path('predict/', pricePredictView.as_view(), name='price'),
    path('predict/<str:category>/', getProduct.as_view(), name='details'),
    path('products/<str:product_id>/stockin', StockInView.as_view(), name='stockin'),
    path('products/<str:product_id>/stockout', StockOutView.as_view(), name='stockout'),
    path('products/graph/<int:month>', graphStockout.as_view(), name='graph'),
]
