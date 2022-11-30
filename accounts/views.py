

from email.mime import base
import imp
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth 
from .forms import ContactForm, EmpForm,ProjectForm
from .models import Project
# from Dashboard import *
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
                auth.login(request,user)
                return render(request,'accounts/login.html')
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return render (request,'base.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('signup')

def home(request):
    return render(request,'index.html')
@login_required
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')


def contact(request):
    
    return render(request,'contact.html')

def feature(request):
    return render(request,'feature.html')
    

  
  
def index(request):
    form = EmpForm
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')  
    context = {'form':form}
    return render(request, 'dashboard.html', context) 

def newproject(request):
    return render(request, 'newproject.html')

def contactres(request):
    form1 =ContactForm
    if request.method == 'POST':
        form1 =ContactForm(request.POST)
        if form1.is_valid():
            form1.save()
            #  redirect('home')  
    context = {'form':form1}
    return render(request, 'success.html', context)  



def addproject(request):
    form2 = ProjectForm
    if request.method == 'POST':
        form2 = ProjectForm(request.POST)
        if form2.is_valid():
            form2.save()
            # redirect('home')  
    context = {'form2':form2}
    return render(request,'success.html',context)


def displayprojects(request):
    obj = Project.objects.all
    context = {
        "obj":obj
    }
    return render(request, 'displayprojects.html',context)

def removeproject(request, prj_id = 0):
    if prj_id:
        try:
            prj = Project.objects.get(id = prj_id)
            print(prj)
            prj.delete()
            return HttpResponse("project successfully deleted")
        except:
             return HttpResponse("enter valid prj id")

    obj1 = Project.objects.all
    context = {
        "obj1":obj1
    }
    return render(request,'removeproject.html',context)

# def successfully_removed(request):
#     obj1 = Project.objects.all
#     context = {
#         "obj1":obj1
#     }
#     return render(request,'removeproject.html',context)

def kanban(request):
    return render(request,'kanban.html')