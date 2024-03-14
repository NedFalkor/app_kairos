from django.db import models


class ChannelVideo(models.Model):
    video_title = models.CharField(max_length=255, unique=True)
    video_data = models.TextField()
    video_thumbnail = models.ImageField(upload_to='videos/thumbnails/', blank=True, null=True)
    video_description = models.TextField(max_length=150, blank=True)
    video_likes = models.IntegerField(default=0)
    video_dislikes = models.IntegerField(default=0)
    video_upload_time = models.DateTimeField(auto_now_add=True)
    video_views = models.IntegerField(default=0)
    categories = models.ManyToManyField('Category', related_name='videos')
    video_file = models.FileField(upload_to='channel_videos/', null=True, blank=True)

    def __str__(self):
        return self.video_title

