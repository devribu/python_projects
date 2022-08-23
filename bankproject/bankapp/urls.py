from . import views
from django.urls import path, include

app_name = 'bankapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('application/', views.application, name='application'),
]
