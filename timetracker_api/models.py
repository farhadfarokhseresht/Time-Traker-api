from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)


class Tags(models.Model):
    name = models.CharField(max_length=150)


class TimeTracker(models.Model):
    description = models.CharField(max_length=300,blank=True,null=True,default=None)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True,null=True,default=None)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE,blank=True,null=True,default=None)
    billable = models.BooleanField(default=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True,null=True,default=None)
