from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=50)
    collegeName = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    rollNo = models.IntegerField()

    def __str__(self):
        return self.name