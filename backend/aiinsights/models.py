import uuid
from django.db import models
from django.conf import settings

class AIInsight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='insights')
    type = models.CharField(max_length=50, help_text="카드 종류 (예: Focus, Schedule)")
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_dismissed = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ai_insights'