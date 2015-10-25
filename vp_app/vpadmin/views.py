from django.shortcuts import render
from django.http import HttpResponse

# JSON support
# from django.core import serializers
import json

# models
from django.contrib.auth.models import User
from .models import Volunteer, TaskLocation, ShiftLog, VolunteerRequest

#CSRF exemption for testing
from django.views.decorators.csrf import csrf_exempt

#time and dates
from datetime import datetime
import time

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

@csrf_exempt
def checkout(request):
    co_data = json.loads(request.body)
    co_timestamp = datetime.fromtimestamp(co_data['time']/1000.0)
    co_logged_by = User.objects.get(pk=co_data['logged_by'])
    print(co_logged_by)
    print(co_timestamp)
    for user in co_data['users']:
        vol = User.objects.get(pk=user['id'])
        shiftlog_new = ShiftLog(volunteer=vol, co_logged_by = co_logged_by, check_out = co_timestamp)
        shiftlog_new.save()
    return HttpResponse('{"result": "success"}')