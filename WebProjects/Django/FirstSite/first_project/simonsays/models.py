from django.db import models

# Create your models here.

class Player(models.Model):
    nickname = models.CharField(max_length=150)
    highscore = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname
