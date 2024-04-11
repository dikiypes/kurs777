from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .pagination import HabitPagination
from .permissions import OwnerPermission, PublicHabitPermission
from .serializers import HabitSerializer
from .models import Habit


class HabitListView(generics.ListCreateAPIView):
    """Представление вывода списка привычек"""
    permission_classes = [IsAuthenticated, OwnerPermission | PublicHabitPermission]
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(Q(user=user) | Q(publicity_flag=True))
        return queryset


class HabitDetailView(generics.RetrieveAPIView):
    """Представление вывода привычки"""
    permission_classes = [IsAuthenticated, OwnerPermission | PublicHabitPermission]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateView(generics.CreateAPIView):
    """Представление создания Привычки"""
    permission_classes = [IsAuthenticated]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDeleteView(generics.DestroyAPIView):
    """Представление удаления Привычки"""
    permission_classes = [IsAuthenticated, OwnerPermission]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    """Представление изменения Привычки"""
    permission_classes = [IsAuthenticated, OwnerPermission]
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
