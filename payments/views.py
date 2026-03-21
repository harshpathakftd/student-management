from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from enrollments.models import Enrollment
from datetime import date


# =========================
# ➕ ADD PAYMENT
# =========================
def add_payment(request):
    enrollments = Enrollment.objects.select_related('student', 'course')

    if request.method == 'POST':
        enrollment_id = request.POST.get('enrollment')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')

        if enrollment_id and amount and due_date:
            Payment.objects.create(
                enrollment_id=enrollment_id,
                amount=amount,
                due_date=due_date
            )
            return redirect('payment_list')

    return render(request, 'payments/add.html', {
        'enrollments': enrollments
    })


# =========================
# 📋 PAYMENT LIST
# =========================
def payment_list(request):
    payments = Payment.objects.select_related(
        'enrollment',
        'enrollment__student',
        'enrollment__course'
    ).order_by('-id')

    return render(request, 'payments/list.html', {
        'payments': payments
    })


# =========================
# ✅ MARK AS PAID
# =========================
def mark_paid(request, id):
    payment = get_object_or_404(Payment, id=id)

    payment.paid = True
    payment.payment_date = date.today()   # 🔥 IMPORTANT
    payment.save()

    return redirect('payment_list')