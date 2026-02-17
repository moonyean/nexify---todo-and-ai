from django.db import models

# Create your models here.

class ChatMessages(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4, raw = True)
    user_id = models.ForeignKey('users.Users', on_delete = models.CASCADE)
    role = models.TextChoices("user", "ai")
    content = models.TextField(null=True) 
    created_at = models.DateTimeField(default=models.timezone.now)

    class Meta:
            db_table = 'chat_messages'