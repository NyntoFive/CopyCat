from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, Shop

# List Product skus by Shop
class CkkListView(ListView):
    template_name = "ckk/split.html"
    queryset = Product.objects.all

# Buttons on a Template!
class DIYView(TemplateView):
    template_name = "ckk/diy.html"
    queryset = Product.objects.all