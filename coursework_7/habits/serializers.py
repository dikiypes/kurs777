from rest_framework import serializers
from .models import Habit
from .validators import HabitPleasureValidator, HabitRewardOrRelatedValidator, HabitTimeForExecutionValidator, \
    HabitPeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор Привычек"""
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)
        validators = [
            HabitPleasureValidator(),
            HabitRewardOrRelatedValidator(),
            HabitTimeForExecutionValidator(),
            HabitPeriodicityValidator()
        ]
