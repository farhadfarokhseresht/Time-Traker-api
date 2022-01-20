from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)


class TimeTracker(models.Model):
    description = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tags = models.CharField(max_length=300)
    billable = models.BooleanField(default=False)
    start_at = models.DateField()
    end_at = models.DateField()
