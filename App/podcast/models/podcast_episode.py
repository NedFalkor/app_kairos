from django.utils import timezone

from django.db import models

from App.podcast.models.podcast import Podcast
from Users.models import CustomUser


class PodcastEpisode(models.Model):
    podcast = models.ForeignKey(Podcast, related_name='episodes', on_delete=models.CASCADE)
    podcast_episode_number = models.PositiveIntegerField()
    podcast_episode_lay_count = models.PositiveIntegerField(default=0)
    podcast_episode_title = models.CharField(max_length=255)
    podcast_episode_description = models.TextField()
    podcast_episode_length = models.DurationField()
    explicit = models.BooleanField(default=False)
    podcast_episode_audio_file = models.FileField(upload_to='podcasts/episodes/')
    podcast_episode_publish_date = models.DateTimeField(default=timezone.now)
    podcast_episode_creator = models.ForeignKey(CustomUser, related_name='created_episodes', on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    podcast_episode_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        unique_together = ('podcast', 'episode_number')

    def __str__(self):
        return f"{self.title} - {self.podcast.title}"