from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)


class Tags(models.Model):
    name = models.CharField(max_length=150)


class TimeTracker(models.Model):
    description = models.CharField(max_length=300,blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE,blank=True)
    billable = models.BooleanField(default=False,blank=True)
    start_at = models.DateField()
    end_at = models.DateField(blank=True)
