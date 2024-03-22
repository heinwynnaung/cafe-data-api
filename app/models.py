from django.db import models
from django.utils import timezone

class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"
