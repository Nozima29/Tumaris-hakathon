from django.contrib import admin

# Register your models here.
from products.models import Products, ProductRate, Category

admin.site.register(Products)
admin.site.register(ProductRate)
admin.site.register(Category)

