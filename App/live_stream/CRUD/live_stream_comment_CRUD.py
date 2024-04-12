from django.utils import timezone
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from app_kairos.App.live_stream.models.live_stream_comment import LiveStreamComment
from app_kairos.App.live_stream.serializers.live_stream_comment_serializer import LiveStreamCommentSerializer


class LiveStreamCommentViewSet(viewsets.ModelViewSet):
    queryset = LiveStreamComment.objects.all()
    serializer_class = LiveStreamCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the comment user to the currently authenticated user
        serializer.save(live_stream_comment_user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        # Ensure only the user who made the comment or an admin can delete it
        if comment.live_stream_comment_user != request.user and not request.user.is_staff:
            return Response({"error": "You do not have permission to delete this comment."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if 'live_stream' in request.query_params:
            self.queryset = self.queryset.filter(
                live_stream_id=request.query_params['live_stream'],
                live_stream__live_stream_is_active=True,
                live_stream__live_stream_start_time__lte=timezone.now(),
                live_stream__live_stream_end_time__gte=timezone.now()
            )
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
