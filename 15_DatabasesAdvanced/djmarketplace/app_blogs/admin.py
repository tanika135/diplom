from django.contrib import admin
from app_blogs.models import Blog, Post, Author


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
