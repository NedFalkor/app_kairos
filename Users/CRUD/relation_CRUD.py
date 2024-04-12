from django.db import models
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from Users.models.relation import Relation
from Users.serializers.relation_serializer import RelationSerializer


class RelationCRUD(viewsets.ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_follower=self.request.user)

    def destroy(self, request, *args, **kwargs):
        relation = self.get_object()
        if relation.user_follower == request.user or relation.user_following == request.user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        user = self.request.user
        return Relation.objects.filter(models.Q(user_follower=user) | models.Q(user_following=user))
