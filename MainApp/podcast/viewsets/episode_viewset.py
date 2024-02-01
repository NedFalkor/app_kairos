# views.py

from rest_framework import viewsets

from MainApp.podcast.models.episode import Episode
from MainApp.podcast.serializers.episode_serializer import EpisodeSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
