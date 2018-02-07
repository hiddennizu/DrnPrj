from django.db import models
from django.utils import timezone
from Course.models import Course
from Batch.models import Batch
from Section.models import Section

gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not Specified', 'Not Specified')
)
blood_group = (
    ('Unknown', 'Unknown'),
    ('A+ve', 'A+ve'),
    ('A-ve', 'A-ve'),
    ('B+ve', 'B+ve'),
    ('B-ve', 'B-ve'),
    ('AB+ve', 'AB+ve'),
    ('AB-ve', 'AB-ve'),
    ('O+ve', 'O+ve'),
    ('O-ve', 'O-ve'),
)


# Create your models here.



class Student(models.Model):
    admission_date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    gender = models.CharField(max_length=20, null=False, choices=gender, default='Not Specified')
    blood_group = models.CharField(max_length=20, null=False, choices=blood_group, default='Unknown')
    birth_place = models.CharField(max_length=120, null=True)
    nationality = models.CharField(max_length=120, null=False, default='Nepal')
    mother_tongue = models.CharField(max_length=40, null=True)

    religion = models.CharField(max_length=60)

    # contact Details
    permanent_address = models.CharField(max_length=60, null=True, blank=True)
    temporary_address = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=60, null=True, blank=True)
    pin_code = models.CharField(max_length=60, null=True, blank=True)
    Country = models.CharField(max_length=60, null=False, default='Nepal')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)

    # Batch details
    course = models.ForeignKey(Course)
    batch = models.ForeignKey(Batch)
    section = models.ForeignKey(Section)
    roll_no = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.first_name
