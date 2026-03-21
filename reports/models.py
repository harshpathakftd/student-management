from django.db import models
from django.contrib.auth.models import User

def upload_report(instance, filename):
    return f"reports/{instance.report_type}/{filename}"

class ReportLog(models.Model):

    REPORT_TYPES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_report, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.report_type} - {self.generated_at.strftime('%Y-%m-%d %H:%M')}"