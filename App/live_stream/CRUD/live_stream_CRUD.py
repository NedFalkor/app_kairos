from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone

from app_kairos.App.live_stream.models.live_stream import LiveStream
from app_kairos.App.live_stream.models.live_stream_comment import LiveStreamComment
from app_kairos.App.live_stream.serializers.live_stream_serializer import LiveStreamSerializer


class LiveStreamCRUD(viewsets.ModelViewSet):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Attribue des permissions dynamiquement en fonction de l'action."""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        livestream = self.get_object()
        livestream.live_stream_is_active = True
        livestream.save()
        return Response({'status': 'livestream activated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        livestream = self.get_object()
        livestream.live_stream_is_active = False
        livestream.save()
        return Response({'status': 'livestream deactivated'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def live_now(self, request):
        # Filtre pour obtenir les livestreams actuellement en direct
        livestreams = LiveStream.objects.filter(live_stream_is_active=True,
                                                live_stream_start_time__lte=timezone.now(),
                                                live_stream_end_time__gte=timezone.now())
        serializer = self.get_serializer(livestreams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def past_livestreams(self, request):
        # Récupère les livestreams qui se sont déjà déroulés
        past_livestreams = LiveStream.objects.filter(live_stream_end_time__lt=timezone.now())
        serializer = self.get_serializer(past_livestreams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def upcoming_livestreams(self, request):
        # Récupère les livestreams prévus pour l'avenir
        upcoming_livestreams = LiveStream.objects.filter(live_stream_start_time__gt=timezone.now())
        serializer = self.get_serializer(upcoming_livestreams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        livestream = self.get_object()
        comment_text = request.data.get('comment_text', None)
        if comment_text:
            LiveStreamComment.objects.create(live_stream=livestream,
                                             live_stream_comment_user=request.user,
                                             live_stream_comment_text=comment_text)
            return Response({'status': 'comment added'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Comment text is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        livestream = self.get_object()
        rating = request.data.get('rating', None)
        if rating is not None:
            try:
                rating = int(rating)
                if 0 <= rating <= 5:
                    livestream.live_stream_rating = rating
                    livestream.save()
                    return Response({'status': 'livestream rated'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Rating must be between 0 and 5'}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({'error': 'Invalid rating value'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Rating value is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        livestream = self.get_object()
        statistics_data = {
            'views': livestream.live_stream_viewer_set.count(),
            'comments': livestream.comments.count(),
            'ratings': livestream.live_stream_rating,
        }
        return Response(statistics_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def schedule(self, request):
        # Logique pour planifier un livestream
        pass

    @action(detail=False, methods=['get'])
    def top_livestreams(self, request):
        top_livestreams = LiveStream.objects.filter(live_stream_is_active=True).order_by('-live_stream_rating')[:5]
        serializer = self.get_serializer(top_livestreams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
