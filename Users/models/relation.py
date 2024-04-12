from django.db import models
from .custom_user import CustomUser


class Relation(models.Model):
    user_follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    user_following = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    relation_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_follower', 'user_following')
        ordering = ['-relation_created_at']

    def __str__(self):
        return f"{self.user_follower.email} follows {self.user_following.email}"
