from .import views
from django.urls import path

app_name = 'travelapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),


]