from django.db import models

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class courseArea(models.Model):
    courseArea = models.CharField(max_length=25)
    course = models.CharField(max_length=30)

class courseDescription(models.Model):
    courseNumber = models.IntegerField
    courseDesc = models.CharField(max_length=50)