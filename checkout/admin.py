from django.contrib import admin
from .models import Order, CartItem
# Register your models here.


@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    pass
    

@admin.register(CartItem)
class Cartadmin(admin.ModelAdmin):
    pass
