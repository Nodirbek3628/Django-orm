from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField( max_length=150)
    category = models.CharField( max_length=150)
    price  = models.IntegerField()
    quantity  = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
