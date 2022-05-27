from django.db import models
from customers.models import Customer
from products.models import Products
# Create your models here.


class Favorites(models.Model):
    customer = models.OneToOneField(
        Customer, related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.customer.full_name


class FavoriteItems(models.Model):
    favorite = models.ForeignKey(
        Favorites, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products, related_name='items', on_delete=models.SET_NULL, null=True)
