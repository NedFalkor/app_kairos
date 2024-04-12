from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

from app_kairos.App.live_stream.models.live_stream_viewer import LiveStreamViewer
from app_kairos.App.live_stream.serializers.live_stream_viewer_serializer import LiveStreamViewerSerializer


class LiveStreamViewerCRUD(viewsets.ModelViewSet):
    queryset = LiveStreamViewer.objects.all()
    serializer_class = LiveStreamViewerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LiveStreamViewer.objects.filter(live_stream__in=self.request.user.livestream_set.all())

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        livestream_viewer = self.get_object()
        livestream_viewer.viewer_join_time = timezone.now()
        livestream_viewer.viewer_status = 'watching'
        livestream_viewer.save()
        return Response({'status': 'joined livestream'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        livestream_viewer = self.get_object()
        livestream_viewer.viewer_leave_time = timezone.now()
        livestream_viewer.viewer_status = 'left'
        livestream_viewer.save()
        return Response({'status': 'left livestream'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def pause(self, request, pk=None):
        viewer = self.get_object()
        viewer.viewer_status = 'paused'
        viewer.save()
        return Response({'status': 'viewer paused'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        livestream = self.get_object().live_stream
        livestream.live_stream_likes += 1
        livestream.save()
        viewer = self.get_object()
        viewer.viewer_likes_count += 1
        viewer.save()
        return Response({'likes_count': livestream.live_stream_likes}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        livestream = self.get_object().live_stream
        livestream.live_stream_dislikes += 1
        livestream.save()
        viewer = self.get_object()
        viewer.viewer_dislikes_count += 1
        viewer.save()
        return Response({'dislikes_count': livestream.live_stream_dislikes}, status=status.HTTP_200_OK)
