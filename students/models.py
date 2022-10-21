from django.db import models



# Create your models here.
class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    email = models.CharField(max_length=75)

    def __str__(self):
        return self.last_name



        



