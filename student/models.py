from django.db import models
from .models import Course

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    courses = models.ManyToManyField(Course)
    email = models.EmailField()
    country = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
