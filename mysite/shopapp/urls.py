from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailsView,
    ProductsListView,
    OrderDetailView,
    OrdersListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderUpdateView,
    OrderDeleteView,
    create_order,
    ProductsExportView,
    OrdersExportView,
    ProductViewSet,
)

app_name = 'shopapp'


routers = DefaultRouter()
routers.register('products', ProductViewSet)


urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('api/', include(routers.urls)),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/export/', ProductsExportView.as_view(), name='products-export'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archive/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/export/', OrdersExportView.as_view(), name='orders-export'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details'),
    path('orders/create', create_order, name='create_order'),
]
