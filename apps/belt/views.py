from django.shortcuts import render, redirect
from .models import User, Trip, Itineraries
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime, date





def index(request):
    userinsession=request.session['user_id']
    logged= User.objects.get(id=request.session['user_id'])
    context= {
    'user': logged,
    'users_trips': Trip.objects.filter(traveler_id=userinsession),
    'trips': Trip.objects.exclude(traveler_id=userinsession)&Trip.objects.exclude(trip_planned__users_id=userinsession),
    'joined_trip':Itineraries.objects.filter(users=userinsession)
    }
    return render(request, 'belt/index.html', context)

def add(request):
    return render(request,'belt/add.html')

def addinfo(request):
    if request.method == 'POST':
        flag=True
        userinsession=request.session["user_id"]
        data={
        'destination': request.POST['destination'],
        'description': request.POST['description'],
        'start': request.POST['start'],
        'end': request.POST['end'],
        'user_id': userinsession
        }

        process=Trip.objects.validator(data)

        if process[0]:
            return redirect(reverse('belt:my_index'))
        else:
            for errs in process[1]:
                messages.error(request, errs)
                return redirect(reverse('belt:add'))

    return render (request,'belt/index.html')

def join(request, id):
    users=User.objects.get(id=request.session['user_id'])
    trips=Trip.objects.get(id=id)
    process=Itineraries.objects.create(users=users, trips=trips)
    return redirect(reverse('belt:my_index'))

def show(request, id):
    userinsession=request.session['user_id']
    location=Trip.objects.get(id=id)
    creator=location.traveler_id
    tripInfo=Itineraries.objects.filter(trips__id=id)&Itineraries.objects.exclude(users_id=creator)

    context={
    "user": userinsession,
    "location": location,
    "tripInfo": tripInfo,
    }
    return render(request, 'belt/trip.html', context)

def logout(request):
    request.session.clear
    return redirect(reverse('login:my_index'))
