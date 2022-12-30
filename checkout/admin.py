from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    pass
    
