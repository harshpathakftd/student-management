from django.shortcuts import render, redirect
from .models import Student


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile']
        )
        return redirect('student_list')

    return render(request,'students/add.html')


def student_list(request):
    return render(request,'students/list.html',{
        'students': Student.objects.all()
    })