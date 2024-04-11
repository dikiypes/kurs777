from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'place', 'time', 'action', 'pleasure_flag',
        'periodicity', 'reward', 'time_for_execution', 'publicity_flag'
    )
    search_fields = ('place', 'action', 'reward')
    list_filter = ('user', 'time', 'pleasure_flag', 'periodicity', 'time_for_execution', 'publicity_flag')
