from django.db import models
from django.conf import settings


class LiveStreamComment(models.Model):
    live_stream = models.ForeignKey('LiveStream', on_delete=models.CASCADE, related_name='comments')
    live_stream_comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='livestream_comments')
    live_stream_comment_text = models.TextField()
    live_stream_comment_created_at = models.DateTimeField(auto_now_add=True)
    live_stream_comment_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.live_stream.title}'
