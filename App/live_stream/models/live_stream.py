from django.db import models
from django.utils import timezone


class LiveStream(models.Model):
    live_stream_title = models.CharField(max_length=255,
                                         unique=True)
    live_stream_data = models.TextField()
    live_stream_thumbnail = models.ImageField(upload_to='thumbnails/',
                                              blank=True,
                                              null=True)
    live_stream_description = models.TextField(max_length=150,
                                               blank=True)
    live_stream_rating = models.DecimalField(max_digits=3,
                                             decimal_places=2,
                                             default=0.00)
    live_stream_start_time = models.DateTimeField(default=timezone.now)
    live_stream_end_time = models.DateTimeField(null=True,
                                                blank=True)
    live_stream_is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.live_stream_title

    @property
    def is_live(self):
        return (self.live_stream_is_active
                and
                self.live_stream_start_time <= timezone.now() <= (self.live_stream_end_time or timezone.now()))
