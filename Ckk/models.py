from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=150)
    image = models.CharField(max_length=200)
    images = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    link = models.URLField()
    breadcrumbs = models.TextField()
    keywords = models.CharField(max_length=200)
    shop = models.PositiveIntegerField()
    origin_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-shop','-origin_date']

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# class Shop(models.Model):
#     def get_highlighted(models.Manager):
