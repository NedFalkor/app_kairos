from rest_framework import serializers

from app_kairos.App.podcast.models.podcast import Podcast
from app_kairos.App.search.models.category import Category


class PodcastSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    episodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = [
            'id', 'podcast_title', 'podcast_description', 'podcast_creator',
            'podcast_cover_image', 'podcast_publish_date', 'categories', 'episodes',
            'podcast_blockchain_txid'
        ]
        read_only_fields = ('podcast_creator',)

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        podcast = Podcast.objects.create(**validated_data)
        podcast.categories.set(categories_data)
        return podcast
