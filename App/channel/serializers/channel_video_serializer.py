from rest_framework import serializers

from App.channel.models.channel_video import ChannelVideo


class ChannelVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelVideo
        fields = '__all__'
