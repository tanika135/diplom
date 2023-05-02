from django.urls import path
from app_goods.views import ItemList


urlpatterns = [
    path('items/', ItemList.as_view(), name='items_list')
]
