from datetime import time
from rest_framework import serializers
from .models import Habit


class HabitPleasureValidator:
    """Валидатор проверки заполнения атрибутов при разных pleasure_flag"""
    def __call__(self, value):
        pleasure_flag = value.get('pleasure_flag')
        reward = value.get('reward')
        related_habit = value.get('related_habit')

        if pleasure_flag:
            if reward or related_habit:
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения и связ. привычки!')

        else:
            if related_habit:
                right_related_habbit = Habit.objects.get(id=related_habit.id)
                if not right_related_habbit.pleasure_flag:
                    raise serializers.ValidationError('Связанная привычка должны быть приятной!')


class HabitRewardOrRelatedValidator:
    """Валидатор проверки одновременного заполнения reward и related_habit"""
    def __call__(self, value):
        reward = value.get('reward')
        related_habit = value.get('related_habit')

        if reward and related_habit:
            raise serializers.ValidationError('Одновременно не может быть вознаграждения и связанной привычки!')


class HabitTimeForExecutionValidator:
    """Валидатор времени выполнения задачи. (не более 120 сек)"""
    def __call__(self, value):
        time_for_execution = value.get('time_for_execution')

        if time_for_execution is not None and time_for_execution > time(0, 2, 0):
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд!')


class HabitPeriodicityValidator:
    """Валидатор проверки периодичности выполнения привычки (не реже 1 раза в 7 дней)"""
    def __call__(self, value):
        periodicity = value.get('periodicity')

        if periodicity is not None and periodicity > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней!')
