from django.shortcuts import render,redirect
from .import models

# SyCode   OldPass    NewPass
def index(request):
  return render(request,'home.html', {})

def test(request):
  DisplayData= models.Test.objects.all()
  return render(request, 'test.html',{'D':DisplayData})

def home(request):
  return render(request,'home.html', {})

def GeneraLinstructions(request):
  return render(request,'GeneraLinstructions.html', {})

def OurTeam(request):
  return render(request,'OurTeam.html', {})