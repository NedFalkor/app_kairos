from django.utils import timezone

from django.db import models

from App.podcast.models.podcast import Podcast
from Users.models import CustomUser


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, related_name='episodes', on_delete=models.CASCADE)
    episode_number = models.PositiveIntegerField()
    play_count = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    length = models.DurationField()
    explicit = models.BooleanField(default=False)
    audio_file = models.FileField(upload_to='podcasts/episodes/')
    publish_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(CustomUser, related_name='created_episodes', on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        unique_together = ('podcast', 'episode_number')

    def __str__(self):
        return f"{self.title} - {self.podcast.title}"