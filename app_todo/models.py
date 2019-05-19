from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()

    deadline = models.DateField(null=True)
    isFinish = models.CharField(max_length=10, default='no')
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.title
