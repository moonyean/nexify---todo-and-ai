from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user_id = models.ForeignKey('users.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, verbose_name = "제목")
    priority = models.TextChoices("High", "Medium", "Low")
    is_done = models.BooleanField(default = False)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
            db_table = 'tasks'

class AiInsights(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user_id = models.ForeignKey('users.User', on_delete = models.CASCADE)
    type = models.TextField(verbose_name = "인사이트 유형")
    title = models.CharField(max_length = 50, verbose_name = "제목")
    content = models.TextField(verbose_name = "내용")
    is_dismissed = models.BooleanField(default = False)

    class Meta:
        db_table = 'ai_insights'

class ChatMessages(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user_id = models.ForeignKey('users.User', on_delete = models.CASCADE)
    role = models.TextChoices("user", "ai")
    content = models.TextField(null=True) 
    created_at = models.DateTimeField(default=timezone.now)

    # user_id = models.ForeignKey(users, on_delete = models.CASCADE)
    # message = models.TextField(verbose_name = "메시지")
    # sender = models.TextChoices("user", "ai")
    # timestamp = models

    def __str__(self):
        return f"{self.sender}: {self.message[:20]}"
    