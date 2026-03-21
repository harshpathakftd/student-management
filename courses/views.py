from django.shortcuts import render, redirect
from .models import Course


def add_course(request):
    if request.method == 'POST':
        Course.objects.create(
            name=request.POST['name'],
            fees=request.POST['fees'],
            duration=request.POST['duration']
        )
        return redirect('course_list')

    return render(request,'courses/add.html')


def course_list(request):
    return render(request,'courses/list.html',{
        'courses': Course.objects.all()
    })