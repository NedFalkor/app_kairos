from rest_framework import permissions


class IsCreatorOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True

            is_creator = hasattr(obj, 'creator') and obj.creator == request.user
            return is_creator

        return False
