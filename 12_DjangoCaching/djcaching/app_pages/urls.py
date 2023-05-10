from django.urls import path
from app_pages.views import welcome, main_page

app_name = 'app_pages'

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('main/', main_page, name='main'),
]
