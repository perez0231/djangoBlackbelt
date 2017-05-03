from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')#CODE HERE

class UserManager(models.Manager):
    def validator(self, data):#self-function, object of function
        flag = True
        errs = []
        if len(data['fname']) < 2:
            flag= False
            errs.append("Cannot have less than 2 characters in First Name")

        if len(data['lname']) < 2:
            flag = False
            errs.append("Cannot have less than 2 characters in Last Name")

        if data['password'] != data['cpassword']:
            flag= False
            errs.append("Passwords do not Match")

        if len(data['password']) < 8:
            flag=False
            errs.append("password must be at least 8 characters long")

        if not EMAIL_REGEX.match(data['email']):
            flag= False
            errs.append("Email not in valid format")
        if  User.objects.filter(email=data['email']):
            flag = False
            errs.append("already in system")

        if flag:
            passverification = data['password']
            hashed = bcrypt.hashpw(str(passverification), bcrypt.gensalt())
            user= User.objects.create(fname= data['fname'],lname=data['lname'], email= data['email'], DOB=data['DOB'], password= hashed)

            return (True, user)
        else: ### else if not true return False spit out errs report
            return(False, errs)

    def login(self, data):
        flag = True
        errs = []
        luser = User.objects.filter(email= data['email'])
        encoded =data['password'].encode()
        print encoded
        if not luser:       #if no email matach will create a QUERY SET, but if returning useer will
            flag= False
            errs.append('Invalid email')
            return (False, errs)
        else:
            if bcrypt.hashpw(encoded, luser[0].password.encode())== luser[0].password:
                flag=True         #checking password
                return (True, luser[0])   #[0]

            else:
                errs.append('invalid password')
                return (False, errs)





class User(models.Model):
    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)
    email = models.EmailField(max_length=55)
    DOB= models.DateTimeField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
