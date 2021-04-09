from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
