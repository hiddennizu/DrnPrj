from django.db import models
from django.utils import timezone
from Course.models import Course
from Batch.models import Batch


class Section(models.Model):
    name = models.CharField(max_length=120)
    course = models.ForeignKey(Course)
    batch = models.ForeignKey(Batch)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
