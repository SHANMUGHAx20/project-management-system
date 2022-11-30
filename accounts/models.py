from __future__ import unicode_literals  
from django.db import models

class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    class Meta:  
        db_table = "student"  

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.TextField()
    class Meta:
        db_table = "contactus"


class Project(models.Model):
    projectname = models.CharField(max_length=25)
    noofppl = models.CharField(max_length=24)
    descr = models.TextField()
    budget = models.IntegerField(null=True)
    deadline = models.DateTimeField(null=True)
    class Meta:
        db_table = "projects"

