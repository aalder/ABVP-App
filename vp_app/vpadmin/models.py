from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(User)
    is_banned = models.BooleanField(default=False, blank=True)
    photo = models.ImageField(upload_to='profiles')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=9)
    emergency_name = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=10)
    emergency_email = models.CharField(max_length=100)

class TaskLocation(models.Model):
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class ShiftLog(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    task_location = models.ForeignKey(TaskLocation)
    logged_by = models.ForeignKey(User)
    check_out = models.DateTimeField(null=True)
    check_in = models.DateTimeField(null=True)
    total_hours = models.IntegerField(null=True)
    
class VolunteerRequest(models.Model):
    task_location = models.ForeignKey(TaskLocation)
    number_volunteers = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


