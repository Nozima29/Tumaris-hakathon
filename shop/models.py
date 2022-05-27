from django.db import models

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    opens_at = models.TimeField()
    closes_at = models.TimeField()
    country = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
