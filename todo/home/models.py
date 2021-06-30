from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Task", null=True)
    taskTitle = models.CharField(max_length=50)
    taskDesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle
    