from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from Users.serializers.register_custom_user_serializer import RegisterCustomUserSerializer

User = get_user_model()


class RegisterUserCRUD(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterCustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')

        # Vérifie si l'email ou le nom d'utilisateur existe déjà
        if User.objects.filter(email=email).exists():
            return Response({"error": "L'email existe déjà"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Le nom d'utilisateur existe déjà"}, status=status.HTTP_400_BAD_REQUEST)

        # Si tout est correct, procède à la création de l'utilisateur
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @classmethod
    def get_extra_actions(cls):
        return []
