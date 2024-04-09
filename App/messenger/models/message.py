from django.db import models

from Users.models import CustomUser


class Message(models.Model):
    TYPE_CHOICES = (
        ('chat', 'Chat'),
        ('mail', 'Mail'),
    )
    message_sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    message_recipient = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    message_content = models.TextField()
    message_sent_at = models.DateTimeField(auto_now_add=True)
    message_received_at = models.DateTimeField(null=True, blank=True)
    message_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='chat')

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'
