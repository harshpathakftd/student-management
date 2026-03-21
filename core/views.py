from django.shortcuts import render
from students.models import Student
from payments.models import Payment
from django.db.models import Sum

def dashboard(request):
    total_students = Student.objects.count()
    total_revenue = Payment.objects.filter(paid=True).aggregate(Sum('amount'))['amount__sum'] or 0
    pending = Payment.objects.filter(paid=False).aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'dashboard.html', {
        'students': total_students,
        'revenue': total_revenue,
        'pending': pending
    })