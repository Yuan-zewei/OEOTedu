from django.shortcuts import render
from .models import Course,Profile

# Create your views here.
def index(request):
    return render(request,'training/index.html')


def show_course(request):
    course=Course.objects.all()
    return render(request,'training/show_course.html',{'course':course})


def show_list(request,id):
    list=Course.objects.get(id=id)
    return render(request,'training/show_list.html',{'list':list})


def all_student(request):
    student=Profile.objects.all()
    return render(request,'training/all_student.html',{'student':student})


