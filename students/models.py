
import uuid
from django.db import models

class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    def save(self,*args,**kwargs):
        if not self.reg_no:
            self.reg_no = f"SOFT-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
