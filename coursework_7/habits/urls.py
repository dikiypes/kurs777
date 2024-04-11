from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitListView, HabitDeleteView, HabitUpdateView, HabitDetailView, HabitCreateView


app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitListView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),
    path('habit/create/', HabitCreateView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_delete'),
]
