from django.db import models
from django.conf import settings


class LiveStreamViewer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    live_stream = models.ForeignKey('LiveStream',
                                    on_delete=models.CASCADE)
    join_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField(null=True,
                                      blank=True)
    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('paused', 'Paused'),
        ('commenting', 'Commenting'),
        ('liking', 'Liking'),
        ('disliking', 'Disliking'),
        ('left', 'Left'),
    ]
    viewer_status = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default='watching')
    viewer_likes_count = models.IntegerField(default=0)
    viewer_dislikes_count = models.IntegerField(default=0)
    viewer_comments_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} viewing {self.live_stream.title}"
