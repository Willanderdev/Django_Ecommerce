
from .views import Product_listView, CategoryListView, product
from django.urls import path

from django.conf.urls.static import static


urlpatterns = [
    
    path('produtos', Product_listView.as_view(), name='produtos'),
    path('category/<slug:slug>', CategoryListView.as_view(), name='category'),
    path('product/<slug:slug>', product, name='product'),
    
]
