from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from App.live_stream.models.live_stream import LiveStream
from App.live_stream.serializers.live_stream_serializer import LiveStreamSerializer


class LiveStreamCRUD(viewsets.ModelViewSet):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        livestream = self.get_object()
        livestream.is_active = True
        livestream.save()
        return Response({'status': 'livestream activated'})

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        livestream = self.get_object()
        livestream.is_active = False
        livestream.save()
        return Response({'status': 'livestream deactivated'})
