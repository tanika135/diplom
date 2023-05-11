from django.urls import path

from .views import (
    AboutMeView, OrdersList, ActionsList
)

app_name = 'app_personal'

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('orders_list/', OrdersList.as_view(), name='orders_list'),
    path('actions/', ActionsList.as_view(), name='actions'),
    path('sales/', OrdersList.as_view(), name='sales'),
    path('balance/', OrdersList.as_view(), name='balance'),
]
