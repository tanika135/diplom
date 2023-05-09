from django.urls import path
from app_static.views import ContactsView, AboutUsView

app_name = 'app_static'

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
]
