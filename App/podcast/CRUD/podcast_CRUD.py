from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response

from app_kairos.App.podcast.models.podcast import Podcast
from app_kairos.App.podcast.serializers.podcast_serializer import PodcastSerializer
from app_kairos.permissions.is_creator_or_admin_permission import IsCreatorOrAdmin


class PodcastCRUD(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['podcast_title', 'podcast_description']
    ordering_fields = ['podcast_publish_date', 'podcast_title']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsCreatorOrAdmin()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(podcast_creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        podcast = self.get_object()
        if podcast.podcast_creator != request.user and not request.user.is_staff:
            return Response({'error': 'Vous n’avez pas la permission de supprimer ce podcast.'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
