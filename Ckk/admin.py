from django.contrib import admin
from .models import Product, Shop

admin.autodiscover()

admin.site.register(Product)
admin.site.register(Shop)
