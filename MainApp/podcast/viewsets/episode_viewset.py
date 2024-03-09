# views.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Podcast
from .serializers import PodcastSerializer
from .permissions import IsCreatorOrAdmin  # Adjust import paths as needed

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsCreatorOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            podcast = serializer.save(creator=request.user)
            categories_ids = request.data.get('categories', [])
            podcast.categories.set(categories_ids)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # No need to override list, retrieve, update, and destroy actions unless custom behavior is needed
