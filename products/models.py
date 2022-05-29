from django.db import models
from django.utils.text import slugify
from customers.models import Customer
from djmoney.models.fields import MoneyField
from shop.models import Inventory
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Types(models.Model):
    category = models.ForeignKey(
        Category, related_name='type', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        Types, related_name='products', on_delete=models.CASCADE, null=True)
    inventory = models.ForeignKey(
        Inventory, related_name='product', on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    discount = models.FloatField('Discount in %', blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True)
    views = models.PositiveIntegerField(default=0)
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    collection = models.CharField(max_length=255, null=True, blank=True)
    avg_rate = models.PositiveIntegerField(default=0)
    price = MoneyField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.name

    @property
    def discount_price(self):
        return self.price - (self.price * self.discount / 100)


class ProductRate(models.Model):
    product = models.ForeignKey(
        Products, related_name='rate', on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, related_name='rate', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
