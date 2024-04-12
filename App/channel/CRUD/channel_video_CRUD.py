from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from app_kairos.App.channel.models.channel_video import ChannelVideo
from app_kairos.App.channel.serializers.channel_video_serializer import ChannelVideoSerializer


class ChannelVideoViewSet(viewsets.ModelViewSet):
    queryset = ChannelVideo.objects.all()
    serializer_class = ChannelVideoSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        video = self.get_object()
        video.video_likes += 1
        video.save()
        return Response({'status': 'like incremented'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        video = self.get_object()
        video.video_dislikes += 1
        video.save()
        return Response({'status': 'dislike incremented'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        video = self.get_object()
        video.video_likes = max(video.video_likes - 1, 0)
        video.save()
        return Response({'status': 'like decremented'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def undislike(self, request, pk=None):
        video = self.get_object()
        video.video_dislikes = max(video.video_dislikes - 1, 0)
        video.save()
        return Response({'status': 'dislike decremented'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def share(self, request, pk=None):
        video = self.get_object()
        video.save()
        return Response({'status': 'video shared'}, status=status.HTTP_200_OK)
