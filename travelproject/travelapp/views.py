from django.shortcuts import render
from .models import Place, Team, Intro
from django.http import HttpResponse


# Create your views here.

def index(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    obj3 = Intro.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2, 'result3':obj3})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
