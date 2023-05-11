from django.contrib import admin
from app_shops.models import Shop, ShopStock, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ShopStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'product', 'stock']
    list_display_links = ['id']
    ordering = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopStock, ShopStockAdmin)
