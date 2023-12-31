from django.contrib import admin
from app_news.models import NewsItem, NewsType, HousingItem, HousingType, NumberOfRooms


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


class HousingItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class HousingTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


class NumberOfRoomsAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'housing']


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(HousingItem, HousingItemAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(NumberOfRooms, NumberOfRoomsAdmin)
