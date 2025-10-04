from django.db import models
from django.contrib.auth.models import User
# name email sab User handel krega

class Task(models.Model):
    # SETNUll,cascade ,null-> child remains if parent is deleted
    # cascade-> if parent is deleted child is also deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']