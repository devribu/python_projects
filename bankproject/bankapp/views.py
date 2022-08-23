from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "index.html")


@login_required(login_url='/')
def welcome(request):
    return render(request, "welcome.html")


@login_required(login_url='/')
def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']

        if name == "" and dob == "" and age == "" and mobile == "" and email == "" and address == "":
            return render(request, 'application.html', {'error':True})
        else:
            messages.info(request, "Application Submitted Successfully")
            return redirect('bankapp:application')

    return render(request, "application.html")
