from django.db import models
from django.contrib.auth.models import User

class Recipie(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')