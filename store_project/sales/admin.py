from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','product','quantity','total_price','created_at')
    search_fields = ('customer__username','product__name')
    list_filter = ('created_at',)