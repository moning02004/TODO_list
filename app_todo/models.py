from django.contrib.auth import get_user_model
from django.db import models


class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    deadline = models.DateField(null=True)
    isFinish = models.CharField(max_length=10, default='no')
    priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
