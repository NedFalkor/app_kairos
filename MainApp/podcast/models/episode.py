from datetime import timezone

from django.db import models

from MainApp.podcast.models.podcast import Podcast
from Users.models import CustomUser


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    audio_file = models.FileField(upload_to='podcasts/episodes/')
    publish_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(CustomUser, related_name='created_episodes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} - {self.podcast.title}"