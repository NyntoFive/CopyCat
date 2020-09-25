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
    category = models.CharField(max_length=50, default="none")
    subcat=models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, null=False, default=0, on_delete=models.CASCADE)
    

    
    objects = ProductManager()
    class Meta:
        ordering = ['sku']
    
    def __str__(self):
        return self.sku


class ProductImage(models.ManyToManyField):
    img = models.ImageField(upload_to="ckk/images", blank=True)
    url = models.URLField()
    image = models.ForeignKey(CKKItem, null=False, default=0, on_delete=models.CASCADE)


class Keywords(models.Model):
    keyword = models.ForeignKey(CKKItem,null=False, default=0,on_delete=models.CASCADE)
    sku = models.CharField(max_length=50)
    
class CKKItem(models.Model):
    images = models.ForeignKey(ProductImage, on_delete=CASCADE)
    sku = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    keyword = models.ForeignKey(Keywords, null=False, default=0, on_delete=models.CASCADE)
    'images', 'videos', 'description', 'keywords', 'url', 'title', 'status_code'

