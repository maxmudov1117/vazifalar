from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class StatusChoices(models.TextChoices):
        NOT_STARTED = '1', 'Yangi'
        IN_PROGRESS = '2', 'Jarayonda'
        COMPLETED = '3', 'Bajarildi'
        
    title = models.CharField(max_length=255)
    deadline = models.DateField(blank=True, null=True)
    details = models.CharField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=StatusChoices.choices, default=StatusChoices.NOT_STARTED)
    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    