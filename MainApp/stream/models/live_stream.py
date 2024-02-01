# MainApp/stream/models.py

from django.db import models
from django.utils import timezone


class LiveStream(models.Model):
    title = models.CharField(max_length=255, unique=True)
    data = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    description = models.TextField(max_length=150, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def is_live(self):
        return self.is_active and self.start_time <= timezone.now() <= (self.end_time or timezone.now())
