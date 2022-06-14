from .models import (StockIn, StockOut)
from rest_framework import serializers
from .models import Product

class pricePredictSerializer(serializers.Serializer):
    category = serializers.CharField()
    id_product = serializers.CharField()
    stock = serializers.IntegerField()
    height = serializers.FloatField()
    width = serializers.FloatField()
    depth = serializers.FloatField()
    cost = serializers.FloatField()
    material = serializers.CharField()

    class Meta:
        model = Product
        fields = ('category','id_product', 'stock', 'height', 'width', 'depth', 'cost', 'material',)


class StockInSerializer(serializers.ModelSerializer):
    added_stock = serializers.IntegerField(min_value=1, max_value=9999999)

    class Meta:
        model = StockIn
        fields = ["product", "added_stock"]


class StockOutSerializer(serializers.ModelSerializer):
    removed_stock = serializers.IntegerField(min_value=1, max_value=9999999)
    your_price = serializers.FloatField(min_value=0.01)

    class Meta:
        model = StockOut
        fields = ["product", "removed_stock", "your_price", "created_date"]
