
from django.urls import path

from .views import CreateCartItemView, CartItemView


urlpatterns = [
    
    path('carrinho/<slug:slug>/', CreateCartItemView.as_view(), name='carrinho'),
    path('cart', CartItemView.as_view(), name='cart'),
    
]
