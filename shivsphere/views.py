from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    return render(request,"home.html",{"current_date": date})

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})

def contact(request):
    return render(request, "contact.html", {})
