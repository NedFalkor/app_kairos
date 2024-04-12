from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={'input_type': 'password'},
                                     min_length=8)
    confirm_password = serializers.CharField(write_only=True,
                                             required=True,
                                             style={'input_type': 'password'},
                                             min_length=8)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def validate(self, data):
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({"email": "Cet email est déjà utilisé."})
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({"username": "Ce nom d'utilisateur est déjà pris."})

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Les mots de passe ne correspondent pas."})

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()

        return user
