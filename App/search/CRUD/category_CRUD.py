from rest_framework import viewsets, permissions

from App.search.models.category import Category
from App.search.serializers.category_serializer import CategorySerializer
from permissions.is_admin_user_or_read_only_permission import IsAdminUserOrReadOnly


class CategoryCRUD(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsAdminUserOrReadOnly]
        return [permission() for permission in permission_classes]