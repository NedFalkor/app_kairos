from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    user_profile_bio = models.TextField(max_length=500, blank=True)
    user_profile_location = models.CharField(max_length=30, blank=True)
    user_profile_website = models.URLField(blank=True)
    user_profile_profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)
    user_profile_created_at = models.DateTimeField(auto_now_add=True)
    user_profile_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.email}"
