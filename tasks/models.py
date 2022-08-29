from django.db import models

# Create your models here.
class Task(models.Model):#creamos nuestra clase tasks con dos campos 
    title= models.CharField(max_length=100)
    description= models.TextField(blank=True)