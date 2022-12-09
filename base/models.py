
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length = 100, null = True)
    email = models.EmailField(unique = True, null = True)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    title =models.CharField(max_length = 50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created', 'completed']
