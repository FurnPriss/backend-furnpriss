from django.db import models
from django.conf import settings
from manager import createProduct

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usr_id')
    id_product = models.CharField(primary_key=True, max_length=255)
    category = models.CharField(max_length=255)
    stock = models.IntegerField()
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    cost = models.FloatField()
    material = models.CharField(max_length=255)
    price = models.FloatField()

    objects = createProduct()

    class Meta:
        ordering = ('id_product',)
