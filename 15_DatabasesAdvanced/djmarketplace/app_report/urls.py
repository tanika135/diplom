from django.urls import path

from .views import report_view


app_name = 'app_report'

urlpatterns = [
    path('', report_view, name='products_list'),
]
