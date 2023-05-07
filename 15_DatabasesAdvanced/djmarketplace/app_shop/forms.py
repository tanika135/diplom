from django import forms

from app_shop.models import Shop, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description'


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = 'name', 'address'
