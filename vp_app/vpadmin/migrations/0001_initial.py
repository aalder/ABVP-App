# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_out', models.DateTimeField(null=True)),
                ('check_in', models.DateTimeField(null=True)),
                ('total_hours', models.IntegerField(null=True)),
                ('logged_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_banned', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to=b'profiles')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=9)),
                ('emergency_name', models.CharField(max_length=100)),
                ('emergency_phone', models.CharField(max_length=10)),
                ('emergency_email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_volunteers', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('task_location', models.ForeignKey(to='vpadmin.TaskLocation')),
            ],
        ),
        migrations.AddField(
            model_name='shiftlog',
            name='task_location',
            field=models.ForeignKey(to='vpadmin.TaskLocation'),
        ),
        migrations.AddField(
            model_name='shiftlog',
            name='volunteer',
            field=models.ForeignKey(to='vpadmin.Volunteer'),
        ),
    ]
