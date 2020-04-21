from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MessageBox(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
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
