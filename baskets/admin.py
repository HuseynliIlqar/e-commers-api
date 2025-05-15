from django.contrib import admin
from .models import Basket, Product, BasketItem,Category

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price',)
    search_fields = ('user__username',)

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'quantity')
    search_fields = ('basket__user__username', 'product__name')
    list_filter = ('basket',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
