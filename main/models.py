from cgitb import text
from turtle import update
from django.db import models
from django.forms import BooleanField, CharField, DateField

# Create your models here.
class Todo(models.Model):
    created_at = models.DataTimeField(auto_now_add=True)
    update_at = models.DataTimeField(auto_now=True)
    name = models.CharField(max_length=200)

class Item(models.Model):
    create_at = models.DataTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    text = models.TextField()
    complete = models.BooleanField(default=False)  
