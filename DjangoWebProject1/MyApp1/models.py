from django.db import models

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class courseArea(models.Model):
    courseArea = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    courseAreaCode = models.CharField(max_length=4, default = "")

class courseDescription(models.Model):
    courseNumber = models.IntegerField
    courseDesc = models.CharField(max_length=50)

class frameworkStandards(models.Model):
    courseAreaCode = models.CharField(max_length=4)
    accreditation = models.CharField(max_length=1)
    year = models.IntegerField()
    frameworkStandards = models.TextField()

class unitData(models.Model):
    course = models.ForeignKey(courseArea, on_delete=models.CASCADE)
    accreditation = models.CharField(max_length=1)
    unitName = models.CharField(max_length=50)
    unitValue = models.FloatField()
    unitGoals = models.TextField()
    unitDesc = models.TextField()
