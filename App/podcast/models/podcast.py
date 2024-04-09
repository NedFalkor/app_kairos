from django.db import models
from django.utils import timezone

from App.search.models.category import Category
from Users.models import CustomUser


class Podcast(models.Model):
    podcast_title = models.CharField(max_length=255)
    podcast_description = models.TextField()
    podcast_creator = models.ForeignKey(CustomUser, related_name='created_podcasts', on_delete=models.SET_NULL, null=True)
    podcast_cover_image = models.ImageField(upload_to='podcasts/covers/', blank=True, null=True)
    podcast_publish_date = models.DateTimeField(default=timezone.now)
    podcast_categories = models.ManyToManyField(Category, related_name='podcasts')
    podcast_blockchain_txid = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title

