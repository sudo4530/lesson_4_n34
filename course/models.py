from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.ManyToManyField(Subject)
    create_date = models.DateField(auto_now=True)





