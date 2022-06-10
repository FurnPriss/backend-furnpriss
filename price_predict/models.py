from django.db import models
from django.conf import settings
from accounts.models import UserModel

class pricePredictModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usr_id')
    product_score = models.FloatField()
    qty = models.FloatField()
    freight_price = models.FloatField()
    product_weight_g = models.FloatField()
    lag_price = models.FloatField()
    comp_1 = models.FloatField()
    ps1 = models.FloatField()
    fp1 = models.FloatField()
    comp_2 = models.FloatField()
    ps2 = models.FloatField()
    fp2 = models.FloatField()
    bed_bath_table = models.FloatField()
    computers_accessories = models.FloatField()
    consoles_games = models.FloatField()
    cool_stuff = models.FloatField()
    furniture_decor = models.FloatField()
    garden_tools = models.FloatField()
    health_beauty = models.FloatField()
    perfumery = models.FloatField()
    watches_gifts  = models.FloatField()
    unit_price = models.FloatField
