from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    ProductCreateView,
    ProductDetailsView,
    ProductsListView,
)


app_name = 'app_shop'

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/', ProductsListView.as_view(), name='products_list'),
]

