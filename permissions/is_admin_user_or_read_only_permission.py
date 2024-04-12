from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows access only to admin users for unsafe methods, but allow read-only access for others.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff