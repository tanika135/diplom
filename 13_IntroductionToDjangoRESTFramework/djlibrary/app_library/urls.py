from django.urls import path
from app_library.views import BookList, AuthorList


urlpatterns = [
    path('books/', BookList.as_view(), name='books_list'),
    path('authors/', AuthorList.as_view(), name='authors_list'),
]
