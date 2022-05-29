from django.db import models
from customers.models import Customer
from products.models import Products
# Create your models here.


class Favorites(models.Model):
    customer = models.OneToOneField(
        Customer, related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_discount(self):
        total = sum(item.discount_price for item in self.items.all())
        return total

    @property
    def total_price(self):
        price = sum(item.product.price for item in self.items.all())
        return price

    def __str__(self) -> str:
        return self.customer.full_name


class FavoriteItems(models.Model):
    favorite = models.ForeignKey(
        Favorites, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products, related_name='items', on_delete=models.SET_NULL, null=True)

    @property
    def discount_price(self):
        discount = self.product.price - \
            (self.product.price * self.product.discount / 100)
        return discount
