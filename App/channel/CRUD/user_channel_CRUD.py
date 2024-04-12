from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from app_kairos.App.channel.models.user_channel import UserChannel
from app_kairos.App.channel.serializers.user_channel_serializer import UserChannelSerializer


class UserChannelCRUD(viewsets.ModelViewSet):
    queryset = UserChannel.objects.all()
    serializer_class = UserChannelSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['subscribe', 'unsubscribe']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(live_stream_user=self.request.user)

    def update(self, request, *args, **kwargs):
        channel = self.get_object()
        if request.user != channel.live_stream_user:
            return Response({'error': 'You do not have permission to update this channel.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Example of customizing the destroy method
        channel = self.get_object()
        if request.user != channel.live_stream_user and not request.user.is_staff:
            return Response({'error': 'You do not have permission to delete this channel.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def subscribe(self, request, pk=None):
        channel = self.get_object()
        channel.channel_subscribers_count += 1
        channel.save()
        return Response({'status': 'subscribed'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unsubscribe(self, request, pk=None):
        channel = self.get_object()
        channel.channel_subscribers_count = max(channel.channel_subscribers_count - 1, 0)
        channel.save()
        return Response({'status': 'unsubscribed'}, status=status.HTTP_200_OK)
