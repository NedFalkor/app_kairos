from rest_framework import serializers

from App.live_stream.models.live_stream_comment import LiveStreamComment


class LiveStreamCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStreamComment
        fields = '__all__'
        read_only_fields = ['live_stream_comment_user', 'live_stream_comment_created_at', 'live_stream_comment_updated_at']