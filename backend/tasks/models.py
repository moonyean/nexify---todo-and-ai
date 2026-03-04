from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, verbose_name = "제목")
    content = models.TextField(verbose_name = "내용", null=True, blank=True)
    priority = models.CharField(max_length = 10, choices = PRIORITY_CHOICES, default = 'Medium')
    is_done = models.BooleanField(default = False)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
            db_table = 'tasks'

    