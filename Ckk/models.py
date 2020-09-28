from django.db import models
from django.urls import reverse
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
    desc_text = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    link = models.URLField()
    breadcrumbs = models.CharField(max_length=200, blank=True)
    metaKeywords = models.CharField(max_length=200)    
    crawled_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, default="none")
    subcategory=models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, null=False, default=0, on_delete=models.CASCADE)
        
    objects = ProductManager()
    class Meta:
        ordering = ['sku']
    
    def __str__(self):
        return self.sku


###############################################################
# Replaces Shop, Product, ProductManager..
class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
# class CKKProduct(models.Model):
#     category = models.ForeignKey(Category,
#                                   related_name='products',
#                                   on_delete=models.CASCADE)
#     sku = models.CharField(max_length=100, db_index=True)
#     name = models.CharField(max_length=200,db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to="CKK/%Y/%m/%d",blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('sku',)
#         index_together = (('id', 'slug'),)

#     def __str__(self):
#         return self.sku
    
#     def get_absolute_url(self):
#         return reverse('shop:product_detail',
#                         args=[self.id, self.slug])


                            

