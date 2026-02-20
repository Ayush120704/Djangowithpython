from django.db import models


# Create your models here.
class amulya(models.Model):
    universityrollnumber=models.IntegerField(unique=True)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255 , unique=True)
