from django.shortcuts import render, redirect
from .models import Enrollment
from students.models import Student
from courses.models import Course


def enroll_student(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        Enrollment.objects.create(
            student_id=request.POST['student'],
            course_id=request.POST['course']
        )
        return redirect('enrollment_list')

    return render(request,'enrollments/add.html',{
        'students': students,
        'courses': courses
    })


def enrollment_list(request):
    data = Enrollment.objects.select_related('student','course')
    return render(request,'enrollments/list.html',{'data': data})