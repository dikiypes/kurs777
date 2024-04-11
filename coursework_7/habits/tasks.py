import requests
from datetime import datetime, timedelta
from config.settings import TG_API_TOKEN
from celery import shared_task
from habits.models import Habit


@shared_task
def send_habit_reminders():
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=2)
    habit_data = Habit.objects.filter(time__gte=start_time)
    url = f"https://api.telegram.org/bot{TG_API_TOKEN}/sendMessage"

    for habit in habit_data:
        params = {
            'chat_id': habit.user.tg_id,
            'text': f"{habit.user.tg_nickname}, в {habit.time} пора сделать {habit.action} в {habit.place}"
        }
        response = requests.post(url, params=params)
        print(response)
