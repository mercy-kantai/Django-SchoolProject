from django.db import models

# Create your models here.
class Class(models.Model):
     class_name = models.CharField(max_length=20)
     class_teacher = models.CharField(max_length=20)
     class_course = models.CharField(max_length=20) 
     class_id = models.PositiveSmallIntegerField()
     class_description = models.TextField()
     class_start_date = models.DateField()
     class_end_date = models.DateField()
     class_size = models.PositiveIntegerField()


     def __str__(self):
        return f"{self.class_name}"

