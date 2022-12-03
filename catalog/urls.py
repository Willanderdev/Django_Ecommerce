
from .views import product_list, category, product
from django.urls import path

from django.conf.urls.static import static


urlpatterns = [
    
    path('produtos', product_list, name='produtos'),
    path('category/<slug:slug>', category, name='category'),
    path('product/<slug:slug>', product, name='product'),
    
]
