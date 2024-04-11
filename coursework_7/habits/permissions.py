from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class PublicHabitPermission(permissions.BasePermission):
    """Позволяет просматривать публичные привычки всем авторизованным пользователям"""
    def has_object_permission(self, request, view, obj):
        if obj.publicity_flag:
            return True
        return False
