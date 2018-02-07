from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

