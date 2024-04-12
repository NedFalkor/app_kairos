from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response

from app_kairos.App.podcast.models.podcast_episode import PodcastEpisode
from app_kairos.App.podcast.serializers.podcast_episode_serializer import PodcastEpisodeSerializer
from app_kairos.permissions.is_creator_or_admin_permission import IsCreatorOrAdmin


class PodcastEpisodeCRUD(viewsets.ModelViewSet):
    queryset = PodcastEpisode.objects.all()
    serializer_class = PodcastEpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['podcast_episode_title', 'podcast_episode_description']
    ordering_fields = ['podcast_episode_publish_date', 'podcast_episode_number', 'podcast_episode_length']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsCreatorOrAdmin, permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(podcast_episode_creator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.podcast_episode_creator:
            instance.podcast_episode_creator = self.request.user
            instance.save()

    def destroy(self, request, *args, **kwargs):
        episode = self.get_object()
        if episode.podcast_episode_creator != request.user and not request.user.is_staff:
            return Response({'error': 'You do not have permission to delete this episode.'},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)

