from rest_framework import serializers

from App.messenger.models.group_chat import GroupChat


class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'
