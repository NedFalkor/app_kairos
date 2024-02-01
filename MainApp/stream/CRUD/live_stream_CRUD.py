from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from MainApp.stream.models.live_stream import LiveStream
from MainApp.stream.serializers.live_stream_serializer import LiveStreamSerializer


class LiveStreamCRUD(viewsets.ModelViewSet):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer

    # Exemple d'une méthode personnalisée pour activer un livestream
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        livestream = self.get_object()
        livestream.is_active = True
        livestream.save()
        return Response({'status': 'livestream activated'})

    # Exemple d'une méthode personnalisée pour désactiver un livestream
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        livestream = self.get_object()
        livestream.is_active = False
        livestream.save()
        return Response({'status': 'livestream deactivated'})

    # Ajoutez d'autres méthodes personnalisées ici si nécessaire
