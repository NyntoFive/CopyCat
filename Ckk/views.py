from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, Shop


class IndexView(ListView):
    template_name = 'ckk/split.html'
    #context_object_name 

    def get_queryset(self):
        """
        Return the last five published questions (not including those set
        to be published in the future.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class CkkListView(ListView):
    template_name = "ckk/split.html"
    queryset = Product.objects.all

class DIYView(TemplateView):
    template_name = "ckk/diy.html"
    queryset = Product.objects.all