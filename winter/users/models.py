from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    gender = models.CharField(max_length = 30, blank = False)

    def __str__(self):
        return self.username