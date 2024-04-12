from rest_framework import permissions


class IsSenderOrRecipient(permissions.BasePermission):
    """
    Permission personnalisée permettant uniquement à l'expéditeur ou au destinataire du message d'accéder au message.
    """

    def has_object_permission(self, request, view, obj):
        # L'accès est autorisé si l'utilisateur est l'expéditeur ou le destinataire du message.
        return obj.message_sender == request.user or obj.message_recipient == request.user
