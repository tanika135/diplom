from django.urls import path
from app_shops.views import page_with_cached_fragments
from .views import (
    ProductDetailsView,
    ProductsListView,
)

app_name = 'app_shops'

urlpatterns = [
    path('page_with_cached_fragments', page_with_cached_fragments, name='page_with_cached_fragments'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/', ProductsListView.as_view(), name='products_list'),
]
