from django.urls import path

from .views import (
    AboutMeView,
)

app_name = 'app_personal'

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about-me'),
]
