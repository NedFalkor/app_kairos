from rest_framework import viewsets

from MainApp.stream.models.viewer import Viewer
from MainApp.stream.serializers.viewer_serializer import ViewerSerializer


class ViewerCRUD(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer
