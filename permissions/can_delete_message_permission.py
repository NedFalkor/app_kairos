from rest_framework import permissions


class CanDeleteMessage(permissions.BasePermission):
    """
    Permission personnalisée permettant uniquement à l'expéditeur du message de le supprimer.
    """

    def has_object_permission(self, request, view, obj):
        # La suppression est autorisée uniquement si l'utilisateur est l'expéditeur du message.
        return obj.message_sender == request.user
