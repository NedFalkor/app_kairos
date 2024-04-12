from rest_framework import serializers

from App.live_stream.models.live_stream_viewer import LiveStreamViewer


class LiveStreamViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStreamViewer
        fields = ['id', 'user', 'live_stream', 'join_time']
        read_only_fields = ('join_time',)