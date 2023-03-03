from django.contrib.auth.models import User
from django.db import models


"""class Notification(models.Model):
    partner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
"""
class Travel(models.Model):
     name=models.CharField(max_length=200)
     passport=models.IntegerField(default=0)
     Date=models.DateTimeField(auto_now_add=True)
     contact=models.IntegerField(default=0)
     country_outside=models.CharField(max_length=200)
     notes=models.CharField(max_length=200)
     

     def __str__(self):
         return self.name

class Partner(models.Model):
     partner_name=models.CharField(max_length=200,unique=True)
     total_amount=models.IntegerField(default=0)
     paid=models.IntegerField(default=0)
     left_to_pay=models.IntegerField(default=0)
     rate_before_starting=models.IntegerField(default=0)
     rate_ready=models.IntegerField(default=0)
#     partner_login=models.CharField(max_length=200,unique=True)
     rate_visa=models.IntegerField(default=0)
     Date=models.DateTimeField(auto_now_add=True)
    

     def __str__(self):
         return self.partner_name

work_permit_choice=(('before process','BEFORE PROCESS'),(('Free','FREE')),('ready','READY'),)
sex_choice=(('male','MALE'),('female','FEMALE'))

class Employee(models.Model):
   employee_name=models.CharField(max_length=200)
   passport_number=models.IntegerField(default=0)
   sex=models.CharField(max_length=14,choices=sex_choice,default="male")
   country=models.CharField(max_length=200)
   nationality=models.CharField(max_length=200)
   work_permit_status=models.CharField(max_length=14,choices=work_permit_choice,default="before processing")
   work_permit_date=models.CharField(max_length=200)
   Date=models.DateTimeField(auto_now_add=True)
   def __str__(self):
         return self.employee_name

class Message(models.Model):
    partner_name = models.ForeignKey(Partner, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(max_length=255, default='partner')
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.partner_name

class Settlement(models.Model):
   partner_name=models.ForeignKey(Partner,on_delete=models.CASCADE)
   settlement_date=models.DateTimeField()
   amount=models.IntegerField(default=0)
   settlement_name=models.CharField(max_length=200)

   def __str__(self):
         return self.partner_name


class Employer(models.Model):
   employer_name=models.CharField(max_length=200)
   position=models.CharField(max_length=200)
   employee_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
   Date=models.DateTimeField(auto_now_add=True)
    
   def __str__(self):
         return self.employee_name

class Document(models.Model):
     passport_photo=models.FileField(upload_to='users/static/uploads/')
     cv=models.FileField(upload_to='users/static/uploads/')
     photo=models.FileField(upload_to='users/static/uploads/')
     employee_name=models.ForeignKey(Employee,on_delete=models.CASCADE)
