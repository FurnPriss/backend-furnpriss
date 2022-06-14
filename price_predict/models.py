from manager.generators import (get_default_date, get_default_id)
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


class Stock(models.Model):
    stock_id = models.CharField(max_length=32, default=get_default_id, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateField(default=get_default_date)

    class Meta:
        abstract = True
        ordering = ["-created_date"]


class StockIn(Stock):
    added_stock = models.PositiveIntegerField()

    class Meta(Stock.Meta):
        pass


class StockOut(Stock):
    removed_stock = models.PositiveIntegerField()
    your_price = models.FloatField()

    class Meta(Stock.Meta):
        pass
