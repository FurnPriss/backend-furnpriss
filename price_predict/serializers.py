from rest_framework import serializers
from .models import pricePredictModel

class pricePredictSerializer(serializers.Serializer):
    category = serializers.CharField()
    qty = serializers.FloatField()
    product_weight_g = serializers.FloatField()
    comp_1 = serializers.FloatField()
    ps1 = serializers.FloatField()

    class Meta:
        model = pricePredictModel
        fields = ('category', 'qty', 'product_weight_g', 'comp1', 'ps1')
