from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.utils import timezone


class User(AbstractUser):
    @property
    def is_councellor(self):
        if hasattr(self, 'councellor'):
            return True
        return False

    @property
    def is_assistant(self):
        if hasattr(self, 'assistant'):
            return True
        return False



class Councellor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Assistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=70)
    student_nuid = models.IntegerField()
    student_major = models.CharField(max_length=50)
    date = models.DateField(db_index=True)
    time = models.TimeField()


    def __str__(self):
        return "Appointment with %s on %s at %s" % (self.student_name, self.date, self.time)


class Attendance(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, null=True)
    councellor = models.ForeignKey(Councellor, on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)
    hold_removed = models.BooleanField(default=False)

    def __str__(self):
        return "Attendance for appointment %s: %s" % (self.appointment, self.attendance)
