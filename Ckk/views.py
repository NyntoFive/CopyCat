from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, Shop

# List Product skus by Shop
class CkkListView(ListView):
    template_name = "ckk/split.html"
    model = Product

# Buttons on a Template!
class DIYView(TemplateView):
    template_name = "ckk/diy.html"
    queryset = Product.objects.all()

# Detail View 1
class CkkDetailView(DetailView):
    template_name = "ckk/detail.html"
    model = Product
    
    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        return reverse('ckk:detail1',
                        args=[self.id, self.slug])
# Detail View 1
class CkkDetailView2(DetailView):
    template_name = "ckk/detail2.html"
    model = Product
    
    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        return reverse('ckk:detail2',
                        args=[self.id, self.slug])
