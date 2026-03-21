from django.db import models
from enrollments.models import Enrollment

class Payment(models.Model):

    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('card', 'Card'),
    )

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

    amount = models.IntegerField()

    due_date = models.DateField()

    paid = models.BooleanField(default=False)

    payment_date = models.DateField(null=True, blank=True)

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        null=True,
        blank=True
    )

    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.enrollment.student.name} - {self.amount}"