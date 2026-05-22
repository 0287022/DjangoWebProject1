from django.db import models

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class courseArea(models.Model):
    courseArea = models.CharField(max_length=30)
    courseAreaCode = models.CharField(max_length=4, default = "")
    def __str__(self): return self.courseArea

class courseDescription(models.Model):
    courseNumber = models.IntegerField
    courseDesc = models.CharField(max_length=50)

    def __str__(self):
        return self.courseDesc

class frameworkStandards(models.Model):
    courseAreaCode = models.CharField(max_length=4)
    accreditation = models.CharField(max_length=1)
    year = models.IntegerField()
    frameworkStandards = models.TextField()

    def __str__(self):
        return self.courseAreaCode

class courseData(models.Model):
    course = models.ForeignKey(courseArea, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=40)
    def __str__(self): return self.courseName

class courseForm(models.Model):
    # This model is here to make it easier to pull data to create dependent dropdown forms
    name=models.CharField(max_length=20)
    course = models.ForeignKey(courseData, on_delete=models.SET_NULL, blank=True, null=True)
    courseArea = models.ForeignKey(courseArea, on_delete=models.SET_NULL, blank=True, null=True)

class unitData(models.Model):
    # Search parameters:
    course = models.ForeignKey(courseData, on_delete=models.CASCADE)
    accreditation = models.CharField(max_length=1)
    year = models.IntegerField()
    # Data holding parameters:
    unitName = models.CharField(max_length=50)
    unitValue = models.FloatField()
    unitGoals = models.TextField()
    unitDesc = models.TextField()
    def __str__(self):
        return self.unitName