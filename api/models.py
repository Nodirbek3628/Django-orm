from django.db import models

class Product(models.Model):
    name = models.CharField( max_length=150)
    category = models.CharField( max_length=150)
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    quantity  = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product (id ={self.id}, name = {self.name})"
