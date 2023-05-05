from django.contrib import admin

from app_shop.models import Product, Shop


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    list_display_links = ['id', 'name']
    ordering = ['id']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']
    list_display_links = ['id', 'name']
    ordering = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)

