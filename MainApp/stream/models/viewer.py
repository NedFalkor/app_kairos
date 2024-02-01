from django.db import models
from django.conf import settings


class Viewer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    live_stream = models.ForeignKey('LiveStream', on_delete=models.CASCADE)
    join_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewing {self.live_stream.title}"
