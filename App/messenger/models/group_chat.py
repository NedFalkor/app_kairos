from django.db import models
from Users.models import CustomUser
from .message import Message


class GroupChat(models.Model):
    group_chat_title = models.CharField(max_length=255)
    group_chat_participants = models.ManyToManyField(CustomUser, related_name='group_chats')
    group_chat_messages = models.ManyToManyField(Message, related_name='group_chat', blank=True)
    group_chat_created_at = models.DateTimeField(auto_now_add=True)
    group_chat_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
