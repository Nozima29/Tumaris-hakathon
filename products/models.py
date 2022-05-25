from django.db import models
from django.utils.text import slugify
from djmoney.models.fields import MoneyField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    discount = models.FloatField('Discount in %', blank=True, null=True)
    price = MoneyField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.name
