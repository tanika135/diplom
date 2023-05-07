from django.urls import path

from .views import post_list


app_name = 'posts_list'

urlpatterns = [
    path('posts_list/', post_list, name='posts_list'),
]
