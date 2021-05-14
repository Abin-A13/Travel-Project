from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='places')
    decspriton = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=250)
    dec = models.TextField()
    image = models.ImageField(upload_to='person')

    def __str__(self):
        return self.name