from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Book
# Student
# Booking

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(default=0, null=True, blank=True)
    count = models.IntegerField(default=1)

    # class Meta:
    #     db_table = "ruslan"

    def __str__(self):
        return f"{self.id} {self.title} {self.description}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20)
    birth_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"

class Booking(models.Model):
    student = models.ManyToManyField(Student)
    book = models.ManyToManyField(Book)
    start_date = models.DateField(auto_now=True)
    returned = models.DateField(null=True)


    def __str__(self):
        return f"{self.id} {self.book} {self.student}"




