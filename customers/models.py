from django.db import models
from django.contrib.auth.models import User
from customers import GENDER_CHOICES
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, related_name='customer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES.choices)
    age = models.PositiveIntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.full_name
