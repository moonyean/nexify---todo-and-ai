from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(max_length = 100, verbose_name = "이메일", unique = True)
    name = models.CharField(max_length = 15, verbose_name = "이름")
    created_at = models.DateTimeField(auto_now_add = True)
    settings = models.JSONField(default = dict)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
    
class LoginSessions(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    deviece_info = models.TextField(verbose_name = "디바이스 정보")
    ip_address = models.GenericIPAddressField(verbose_name = "IP 주소")
    login_at = models.DateTimeField(default=timezone.now)
    is_current = models.BooleanField(default=False)

    class Meta:
            db_table = 'login_sessions'