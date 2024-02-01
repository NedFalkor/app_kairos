# MainApp/stream/models.py

class Video(models.Model):
    title = models.CharField(max_length=255, unique=True)
    data = models.TextField()
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', blank=True, null=True)
    description = models.TextField(max_length=150, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
