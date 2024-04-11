from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Модель "Привычка" """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.CharField(max_length=150, verbose_name="Место")
    time = models.TimeField(default='00:00:00', verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие (привычка)")
    pleasure_flag = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность (в днях)")
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    time_for_execution = models.TimeField(default='00:01:00', verbose_name="Время на выполнение")
    publicity_flag = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
