import datetime

from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500)
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    image = models.URLField(max_length=2000)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"
    

