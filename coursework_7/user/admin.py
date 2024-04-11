from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'tg_nickname', 'last_name', 'avatar', 'phone_number',)
    search_fields = ('email', 'first_name', 'last_name', 'tg_nickname')
