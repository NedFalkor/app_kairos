from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthCustomUserSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        user = authenticate(email=email_or_username, password=password)
        if not user:
            user = authenticate(username=email_or_username, password=password)

        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")

        attrs['user'] = user
        return attrs
