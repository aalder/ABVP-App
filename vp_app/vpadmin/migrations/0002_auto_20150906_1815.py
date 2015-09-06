# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='emergency_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='emergency_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='emergency_phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'profiles'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='zipcode',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
