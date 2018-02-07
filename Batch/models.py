from django.db import models
from django.utils import timezone
from Course.models import Course


# Create your models here.
class Batch(models.Model):
    name = models.CharField(max_length=120)
    course = models.ForeignKey(Course)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(auto_now_add=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
