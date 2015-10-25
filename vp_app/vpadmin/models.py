from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from datetime import date

class Volunteer(models.Model):
    user = models.OneToOneField(User)
    is_banned = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='profiles', null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=9, null=True)
    birthdate = models.DateField(auto_now=False, null=True)
    emergency_name = models.CharField(max_length=100, null=True)
    emergency_phone = models.CharField(max_length=10, null=True)
    emergency_email = models.CharField(max_length=100, null=True)

    def as_json(self):
        return dict(
            id=self.id, 
            username = self.user.username,
            first_name = self.user.first_name,
            last_name = self.user.last_name,
            phone=self.phone, 
            address=self.address,
            state=self.state,
            zipcode=self.zipcode,
            birthdate=str(self.birthdate),)

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


