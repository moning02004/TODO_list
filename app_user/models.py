from django.contrib.auth.models import User
from django.db import models

from app_todo.models import Todo


class MessageBox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unread = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username + '\'s message' + str(self.unread)


class Message(models.Model):
    box = models.ForeignKey(MessageBox, on_delete=models.CASCADE)
    target = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.content

    def save(self, **kwargs):
        self.box.unread += 1
        self.box.save()
        super(Message, self).save()

    def get_todo(self):
        return Todo.objects.get(pk=int(self.target))