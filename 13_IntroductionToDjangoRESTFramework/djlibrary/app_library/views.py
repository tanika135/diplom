from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_library.serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import GenericAPIView
from app_library.models import Book, Author


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
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


