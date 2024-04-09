# serializers.py

from rest_framework import serializers

from app_kairos.App.podcast.models.podcast_episode import PodcastEpisode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastEpisode
        fields = '__all__'
