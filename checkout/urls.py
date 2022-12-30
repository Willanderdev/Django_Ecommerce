
from django.urls import path

from .views import CreateCartItemView, CartItemView, CheckoutView, OrderListView, OrderDetailView, PaypalView


urlpatterns = [
    
    path('carrinho/<slug:slug>/', CreateCartItemView.as_view(), name='carrinho'),
    path('cart/', CartItemView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('meus_pedidos/', OrderListView.as_view(), name='order_list'),
    path('meus_pedidos/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('finalizando/<int:pk>/paypal', PaypalView.as_view(), name='paypal'),
    
]
