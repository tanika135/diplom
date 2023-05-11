from django.contrib import admin
from app_users.models import Profile, Balance


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['id']


class BalanceAdmin(admin.ModelAdmin):
    model = Balance
    list_display = ['id']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Balance, BalanceAdmin)
