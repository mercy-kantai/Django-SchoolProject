from django.db import models
from .models import Student
from .models import Course


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code_id = models.PositiveSmallIntegerField()
    country = models.CharField()
    course_taught = models.OneToOneField(Course)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    phone_number = models.CharField()
    department = models.CharField()
    office_hours = models.CharField()
    bio = models.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    