from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_duration = models.TimeField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_description = models.TextField()
    course_id = models.PositiveSmallIntegerField()
    course_teacher = models.CharField()
    course_department = models.CharField()
    course_syllabus = models.FileField()
    course_status = models.CharField(max_length=20,  choices=[('Active', 'Active'), ('Inactive', 'Inactive')])


    def __str__(self):
        return f'{self.course_name}'
     