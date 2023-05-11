from django.urls import path

from .views import (
    AboutMeView,
    OrdersList,
    ActionsList,
    BalanceView,
    OffersList,
)

app_name = 'app_personal'

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('orders_list/', OrdersList.as_view(), name='orders_list'),
    path('actions/', ActionsList.as_view(), name='actions'),
    path('offers/', OffersList.as_view(), name='offers'),
    path('balance/', BalanceView.as_view(), name='balance'),
]
