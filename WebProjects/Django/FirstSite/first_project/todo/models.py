from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Items(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item
