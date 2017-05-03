from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def rprocess(request):
    data = {
        "fname": request.POST['fname'],
        "lname": request.POST['lname'],
        "email": request.POST['email'],
        "DOB": request.POST['DOB'],
        "password": request.POST['password'],
        "cpassword": request.POST['cpassword']
    }
    results = User.objects.validator(data)

    if results[0]:
        request.session['user_id']= results[1].id
        return redirect ("/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect("/")
def success(request):
    # return render(request, 'success.html', context)
    return redirect(reverse('belt:my_index'))

def login(request):
    data = {
    "email": request.POST['email'],
    "password": request.POST['password'],
    }
    results = User.objects.login(data)

    if results[0]:
        request.session['user_id']= results[1].id
        return redirect ("/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect ("/")
