from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User
from .models import Habit


class HabbitTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self):
        """Вводные для тестирования"""
        self.user = User.objects.create(email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.data = {
            'place': 'Москва',
            'time': '00:00:00',
            'action': 'Попить воды',
            'pleasure_flag': False,
            'periodicity': 7,
            'time_for_execution': '00:02:00',
            'publicity_flag': False,
            'reward': 'Отжаться 10 раз',
        }
        self.habit = Habit.objects.create(user=self.user, **self.data)

    def test_create_habit(self):
        """Создания привычки"""
        response = self.client.post(reverse('habits:habit_create'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(), {
                'id': 2,
                'place': 'Москва',
                'time': '00:00:00',
                'action': 'Попить воды',
                'pleasure_flag': False,
                'periodicity': 7,
                'time_for_execution': '00:02:00',
                'publicity_flag': False,
                'reward': 'Отжаться 10 раз',
                'user': 1,
                'related_habit': None
            }
        )
        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):
        """получение списка привычек"""
        response = self.client.get(reverse('habits:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    'id': 1,
                    'place': 'Москва',
                    'time': '00:00:00',
                    'action': 'Попить воды',
                    'pleasure_flag': False,
                    'periodicity': 7,
                    'time_for_execution': '00:02:00',
                    'publicity_flag': False,
                    'reward': 'Отжаться 10 раз',
                    'user': 1,
                    'related_habit': None
                }
            ]
        })

    def test_habit_retrieve(self):
        """получение привычки"""
        response = self.client.get(reverse('habits:habit_detail', kwargs={'pk': self.habit.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': 1,
            'place': 'Москва',
            'time': '00:00:00',
            'action': 'Попить воды',
            'pleasure_flag': False,
            'periodicity': 7,
            'time_for_execution': '00:02:00',
            'publicity_flag': False,
            'reward': 'Отжаться 10 раз',
            'user': 1,
            'related_habit': None
        })

    def test_habit_destroy(self):
        """Тестирование удаления привычки"""
        response = self.client.delete(reverse('habits:habit_delete', kwargs={'pk': self.habit.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_update(self):
        """изменение привычки"""
        url = reverse('habits:habit_update', kwargs={'pk': self.habit.id})

        response = self.client.patch(url, {'place': 'Питер'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': 1,
            'place': 'Питер',
            'time': '00:00:00',
            'action': 'Попить воды',
            'pleasure_flag': False,
            'periodicity': 7,
            'time_for_execution': '00:02:00',
            'publicity_flag': False,
            'reward': 'Отжаться 10 раз',
            'user': 1,
            'related_habit': None
        })
