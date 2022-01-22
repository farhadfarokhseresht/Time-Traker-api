from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class TimeTracker(models.Model):
    description = models.CharField(max_length=300, blank=True, null=True, default=None)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True,null=True,default=None)
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE,blank=True,null=True,default=None)
    billable = models.BooleanField(default=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.description + " start at : " + str(self.start_at) +" end at : " + str(self.end_at)
