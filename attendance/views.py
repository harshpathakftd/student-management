from django.shortcuts import render, redirect
from .models import Attendance
from students.models import Student


def mark_attendance(request):
    students = Student.objects.all()

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                status=status
            )

        return redirect('dashboard')

    return render(request, 'attendance/mark.html', {
        'students': students
    })


def attendance_list(request):
    records = Attendance.objects.select_related('student').all()

    return render(request, 'attendance/list.html', {
        'records': records
    })