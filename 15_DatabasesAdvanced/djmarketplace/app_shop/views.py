from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from app_shop.forms import ShopForm
from app_shop.models import Product, Shop


class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Product
    fields = 'name', 'price', 'description'
    success_url = reverse_lazy('app_shop:products_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        responce = super().form_valid(form)
        return responce


class ProductDetailsView(DetailView):
    template_name = 'app_shop/product-details.html'
    queryset = Product.objects
    context_object_name = 'product'


class ProductsListView(ListView):
    template_name = 'app_shop/products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ShopCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Shop
    fields = 'name', 'address'
    success_url = reverse_lazy('app_shop:products_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        responce = super().form_valid(form)
        return responce


