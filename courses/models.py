from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name