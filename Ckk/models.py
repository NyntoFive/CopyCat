from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Shop(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def get_shop(self, shop):
        return self.filter(shop__name__iexact=shop)

class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=150)
    image = models.URLField()
    images = models.CharField(max_length=200)
    description = models.TextField()
    desc_txt = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    url = models.URLField()
    breadcrumbs = models.CharField(max_length=200, blank=True)
    metaKeywords = models.CharField(max_length=200)    
    crawled_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, null=False, default=0, on_delete=models.CASCADE)

    tags = TaggableManager()
    objects = ProductManager()
    class Meta:
        ordering = ['sku']
    
    def __str__(self):
        return self.sku

# class Shop(models.Model):
#     def get_highlighted(models.Manager):
