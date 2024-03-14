from django.db import models
from django.conf import settings


class UserChannel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel')
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='user_channels')
    channel_description = models.TextField(blank=True, null=True)
    channel_thumbnail = models.ImageField(upload_to='channels/thumbnails/', blank=True, null=True)
    channel_created_at = models.DateTimeField(auto_now_add=True)
    channel_updated_at = models.DateTimeField(auto_now=True)
    channel_subscribers_count = models.IntegerField(default=0)
    live_streams = models.ManyToManyField('LiveStream', related_name='channels', blank=True)
    channel_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} Channel by {self.user.username}"
