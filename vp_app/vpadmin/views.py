from django.shortcuts import render
from django.http import HttpResponse

# JSON support
# from django.core import serializers
import json

# models
from django.contrib.auth.models import User
from .models import Volunteer, TaskLocation, ShiftLog, VolunteerRequest


def index(request):
    volunteers = Volunteer.objects.all()
    # vol_data_all = {}
    # vol_data = {}
    # for vol in volunteers:
    #     vol_data_all['volunteer'] = vol_data
    #     vol_data['username'] = vol.user.username
    #     vol_data['first_name'] = vol.user.first_name

    results = [vol.as_json() for vol in volunteers]

    # vol_data = serializers.serialize('json', volunteers)

    return HttpResponse(json.dumps(results), content_type='jsonp')

def volunteer(request, vol_id):
    volunteer = Volunteer.objects.get(id = vol_id)
    if volunteer is not None:
        results = volunteer.as_json()
        return HttpResponse(json.dumps(results), content_type='jsonp')