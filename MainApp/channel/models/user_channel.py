from django.db import models
from django.conf import settings


class UserChannel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel')
    name = models.CharField(max_length=255, unique=True)
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE, related_name='videos')
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='channels/thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subscribers_count = models.IntegerField(default=0)
    live_streams = models.ManyToManyField('LiveStream', related_name='channels', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} Channel by {self.user.username}"
