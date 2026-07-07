from django.db import models

# Create your models here.
class student(models.Model): #models.Model likhna padta
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    date = models.DateField(null = True)

class hospital(models.Model)    :
    name = models.CharField()

class cars(models.Model):
    name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)