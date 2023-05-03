from django.contrib import admin
from app_library.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'birth_year']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'year', 'pages', 'author']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
