from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_library.serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import GenericAPIView
from app_library.models import Book, Author


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        item_name = self.request.query_params.get('name')
        author = self.request.query_params.get('author')
        if item_name and author:
            queryset = queryset.filter(name=item_name, author=author)

        pages_equal = self.request.query_params.get('pages_eq')
        if pages_equal:
            queryset = queryset.filter(pages=pages_equal)

        pages_larger_than = self.request.query_params.get('pages_gt')
        if pages_larger_than:
            queryset = queryset.filter(pages__gt=pages_larger_than)

        pages_less_than = self.request.query_params.get('pages_lt')
        if pages_less_than:
            queryset = queryset.filter(pages__lt=pages_less_than)

        return queryset

    def get(self, request):
        return self.list(request)


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)


