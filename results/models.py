# IMPORT FROM DJANGO
from django.db import models


class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    class_level = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.roll_number}"


class Subject(models.Model):
    sub_name = models.CharField(max_length=20)

    def __str__(self):
        return self.sub_name


class Exam(models.Model):
    exam_name = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.exam_name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2)


class ResultPublish(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    publish_date = models.DateField()

    def __str__(self):
        return f"Published on {self.publish_date}"
