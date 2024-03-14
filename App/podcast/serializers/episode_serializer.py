# serializers.py

from rest_framework import serializers

from App.podcast.models.podcast_episode import Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'