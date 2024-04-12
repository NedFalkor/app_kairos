from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from app_kairos.App.messenger.models.group_chat import GroupChat
from app_kairos.App.messenger.models.message import Message
from app_kairos.App.messenger.serializers.group_chat_serializer import GroupChatSerializer


class IsParticipantOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow participants of a group chat to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user in obj.group_chat_participants.all()


class GroupChatViewSet(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'add_message', 'remove_message']:
            permission_classes = [permissions.IsAuthenticated, IsParticipantOrReadOnly]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsParticipantOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # Automatically add creator to participants
        group_chat = serializer.save()
        group_chat.group_chat_participants.add(self.request.user)

    @action(detail=True, methods=['post'])
    def add_message(self, request, pk=None):
        group_chat = self.get_object()
        message_id = request.data.get('message_id')
        try:
            message = Message.objects.get(pk=message_id)
            group_chat.group_chat_messages.add(message)
            return Response({'status': 'Message added'}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response({'error': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def remove_message(self, request, pk=None):
        group_chat = self.get_object()
        message_id = request.data.get('message_id')
        try:
            message = Message.objects.get(pk=message_id)
            group_chat.group_chat_messages.remove(message)
            return Response({'status': 'Message removed'}, status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response({'error': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        if self.action in ['list']:
            return GroupChat.objects.filter(group_chat_participants=self.request.user)
        return super().get_queryset()
