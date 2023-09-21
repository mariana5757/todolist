from django.db import models

# Create your models here.
class Tareas(models.Model):
    tarea = models.CharField(max_length=100)