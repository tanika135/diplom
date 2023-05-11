from django.urls import path

from .views import (
    AboutMeView, OrdersList,
)

app_name = 'app_personal'

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('orders_list/', OrdersList.as_view(), name='orders_list'),
]
