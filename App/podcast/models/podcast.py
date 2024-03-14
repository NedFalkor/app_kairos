from django.db import models
from django.utils import timezone

from App.search.models.category import Category
from Users.models import CustomUser


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, related_name='created_podcasts', on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='podcasts/covers/', blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, related_name='podcasts')

    def __str__(self):
        return self.title

