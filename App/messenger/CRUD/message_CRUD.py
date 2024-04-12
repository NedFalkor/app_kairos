from django.contrib.messages.storage.cookie import MessageSerializer
from django.db import models
from rest_framework import viewsets, permissions

from app_kairos.App.messenger.models.message import Message
from app_kairos.permissions.can_delete_message_permission import CanDeleteMessage
from app_kairos.permissions.is_sender_or_recipient_serializer import IsSenderOrRecipient


class MessageCRUD(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [
                IsSenderOrRecipient]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [CanDeleteMessage]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(models.Q(message_sender=user) | models.Q(message_recipient=user))

    def perform_create(self, serializer):
        serializer.save(message_sender=self.request.user)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
