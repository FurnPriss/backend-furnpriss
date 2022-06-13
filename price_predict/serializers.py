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
