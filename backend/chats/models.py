from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class ChatMessages(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user_id = models.ForeignKey('users.User', on_delete = models.CASCADE)
    role = models.TextChoices("user", "ai")
    content = models.TextField(null=True) 
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
            db_table = 'chat_messages'