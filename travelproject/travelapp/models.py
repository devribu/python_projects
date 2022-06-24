from django.db import models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    class Meta:
        db_table: 'travelapp_place'

    def __str__(self):
        return self.name


class Team(models.Model):
    foto = models.ImageField(upload_to='pics2')
    title = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.title


class Intro(models.Model):
    para1 = models.TextField()
    para2 = models.TextField()
    image = models.ImageField(upload_to='pics3')