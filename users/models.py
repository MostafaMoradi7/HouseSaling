from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class MessageModel(models.Model):
    message = models.CharField(max_length=200)
