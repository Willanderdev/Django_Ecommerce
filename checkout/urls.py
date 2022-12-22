
from django.urls import path

from .views import CreateCartItemView, CartItemView, CheckoutView, OrderListView


urlpatterns = [
    
    path('carrinho/<slug:slug>/', CreateCartItemView.as_view(), name='carrinho'),
    path('cart/', CartItemView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('meus_pedidos/', OrderListView.as_view(), name='order_list'),
    
]
