from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code_id = models.PositiveSmallIntegerField()
    country = models.CharField()
    course_taught = models.CharField()
    class_taught = models.CharField()
    phone_number = models.CharField()
    department = models.CharField()
    office_hours = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    