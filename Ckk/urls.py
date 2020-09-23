from .views import CkkListView, DIYView
from django.urls import path
urlpatterns = [
    path('', CkkListView.as_view(),name="ckk"),
    path('diy/', DIYView.as_view(),name="diy"),
    ]