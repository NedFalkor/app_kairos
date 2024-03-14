from rest_framework import serializers

from App.live_stream.models.live_stream import LiveStream


class LiveStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStream
        fields = '__all__'
