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
from datetime import datetime, timedelta
from pytz import timezone
import pytz
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
    # example data
    # { "logged_by": 2,
    #  "time": 1445805128279,
    #  "task": 1,
    #  "users": [{"id": 2},{"id": 3}]
    # }
    try:
        co_data = json.loads(request.body)
        co_timestamp = datetime.fromtimestamp(co_data['time']/1000.0)
        co_logged_by = User.objects.get(pk=co_data['logged_by'])
        co_tasklocation = TaskLocation.objects.get(pk=co_data['task'])
        # print(co_logged_by)
        # print(co_timestamp)
        for user in co_data['users']:
            vol = User.objects.get(pk=user['id'])
            if ShiftLog.objects.filter(volunteer=vol, check_in = None):
                print("Error: " + str(vol.first_name) + " " + str(vol.last_name) + " is already checked out")
            else:
                shiftlog_new = ShiftLog(volunteer=vol, co_logged_by = co_logged_by, check_out = co_timestamp, task_location = co_tasklocation)
                shiftlog_new.save()
        return HttpResponse('{"result": "success"}')
    except Exception:
        return HttpResponse('{"result": "failure"}')

@csrf_exempt
def checkin(request):
    # example data
    # { "logged_by": 3,
    #  "time": 1445810528279,
    #  "task": 1,
    #  "users": [{"id": 2},{"id": 3}]
    # }
    try:
        ci_data = json.loads(request.body)
        ci_timestamp = datetime.fromtimestamp(ci_data['time']/1000.0)
        ci_logged_by = User.objects.get(pk=ci_data['logged_by'])
        ci_tasklocation = TaskLocation.objects.get(pk=ci_data['task'])
        for user in ci_data['users']:
            vol = User.objects.get(pk=user['id'])
            try:
                shiftlog_entry = ShiftLog.objects.filter(volunteer = vol, task_location = ci_tasklocation, check_in = None)[0]

                co_timestamp = shiftlog_entry.check_out.replace(tzinfo=None)
                total_timedelta =  ci_timestamp - co_timestamp
                total_hours = total_timedelta.seconds/60.0/60.0

                print(total_hours)

                shiftlog_entry.total_hours = total_hours
                shiftlog_entry.check_in = ci_timestamp
                shiftlog_entry.ci_logged_by = ci_logged_by
                shiftlog_entry.save()
            except Exception:
                return HttpResponse('{"result": "user ' + str(user['id']) + ' does not have a blank entry"}')        
        return HttpResponse('{"result": "success"}')
    except Exception:
        return HttpResponse('{"result": "failure"}') 

@csrf_exempt
def open_logs(request):
    # try:
    open_entries = []
    log_entries = ShiftLog.objects.filter(check_in = None)
    print(log_entries)
    for entry in log_entries:
        open_entry = {}
        open_entry['task_id'] = entry.task_location.id
        open_entry['task_name'] = entry.task_location.name
        open_entry['task_location'] = entry.task_location.room
        open_entry['user_id'] = entry.volunteer.id
        open_entry['first_name'] = entry.volunteer.first_name
        open_entry['last_name'] = entry.volunteer.last_name
        open_entry['check_out'] = time.mktime(entry.check_out.timetuple())*1000
        open_entries.append(open_entry)
    print(open_entries)
    return HttpResponse(json.dumps(open_entries))

    # except Exception:
    #     return HttpResponse('{"result": "failure"}')

@csrf_exempt
def available_vols(request):
    users = User.objects.filter(is_active = True, is_staff = False)
    checked_out = ShiftLog.objects.filter(check_in = None).values('volunteer')
    print(checked_out)
    # users.exclude(checked_out__)
    print(users)
    available_users = User.objects.exclude(id__in = checked_out)
    print(available_users)
    available_array = []
    for user in available_users:
        available = {}
        available['id'] = user.id
        available['first_name'] = user.first_name
        available['last_name'] = user.last_name
        available_array.append(available)
    return HttpResponse(json.dumps(available_array))
