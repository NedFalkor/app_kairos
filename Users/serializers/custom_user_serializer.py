from rest_framework import serializers

from Users.models.custom_user import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username']
        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'required': True}
        }
