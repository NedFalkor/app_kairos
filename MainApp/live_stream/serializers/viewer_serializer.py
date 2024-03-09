from rest_framework import serializers

from MainApp.live_stream.models.live_stream_viewer import Viewer


class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['id', 'user', 'live_stream', 'join_time']
        read_only_fields = ('join_time',)