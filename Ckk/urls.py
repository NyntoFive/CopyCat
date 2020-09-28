from .views import CkkListView, DIYView, CkkDetailView, CkkDetailView2
from django.urls import path
urlpatterns = [
    path('', CkkListView.as_view(),name="ckk"),
    path('diy/', DIYView.as_view(),name="diy"),
    path('<int:pk>/1', CkkDetailView.as_view(),name="detail1"),
    path('<int:pk>/2', CkkDetailView2.as_view(),name="detail2"),
    ]