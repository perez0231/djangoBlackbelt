from __future__ import unicode_literals
import re
from datetime import date, datetime
from django.db import models
from django.contrib import messages
from ..login.models import User


# Create your models here.
class TripManager(models.Manager):
    def validator(self,data):
        errs= []
        flag=False

        if not data['destination'] or not data['destination'] or not data['start'] or not data['end']:
            flag=True
            errs.append('No entries can be blank!')
        if not data['start'] or not data['end']:
            flag=True
            errs.append('Must enter travel dates!')

        else:
            if data['start']:
                startdate=datetime.strptime(data['start'], '%Y-%m-%d')
            if data['end']:
                enddate= datetime.strptime(data['end'], '%Y-%m-%d')

            if startdate < datetime.now():
                flag=True
                errs.append ('All trips must start on a future datetime')
            if  startdate > enddate:
                flag= True
                errs.append('Travel enddate cannot be before the start of the trip')

        if not flag:
            print data['user_id']
            trip=Trip.objects.create(destination=data['destination'], plan=data['description'], startdate=data['start'], enddate=data['end'], traveler_id=data['user_id'])

            print data['user_id']
            print "*" * 1000
            return (True, trip)

        else:
            return (False, errs)


class Trip(models.Model):
    destination=models.CharField(max_length=100)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    plan=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    traveler=models.ForeignKey(User, related_name="trip_users")
    objects = TripManager()


class Itineraries(models.Model):
    users=models.ForeignKey(User, related_name="going_user")
    trips=models.ForeignKey(Trip, related_name="trip_planned")
