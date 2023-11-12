from django.db import models

# Create your models here.

class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    img_url = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Orders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'