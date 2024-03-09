from rest_framework import viewsets

from MainApp.live_stream.models.live_stream_viewer import Viewer
from MainApp.live_stream.serializers.viewer_serializer import ViewerSerializer


class ViewerCRUD(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer
