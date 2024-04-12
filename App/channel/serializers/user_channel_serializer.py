from rest_framework import serializers

from App.channel.models.user_channel import UserChannel


class UserChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChannel
        fields = '__all__'
