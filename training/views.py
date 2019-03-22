from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from datetime import datetime
from .models import Profile, Post, Company
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
# 主页
def index(request):
    return render(request, 'training/index.html')


# 课程列表
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'training/courses_list.html', {'courses': courses})


# 课程修改功能
def course_edit(request, id):
    course = Course.objects.get(id=id)
    courses = Course.objects.all().filter(teacher__name=request.user.profile.name)
    if request.method == 'POST':
        course_form = CourseForm(data=request.POST, instance=course)
        if course_form.is_valid() and courses:
            for course in courses:
                # 拿到课程的开始时间和结束时间
                time_start = course.starttime
                time_end = course.endtime
                # 得到修改后的课程的开始时间和结束时间
                start = course_form.cleaned_data['starttime']
                end = course_form.cleaned_data['endtime']
                # 符合课程时间的条件为：开始时间大于结束时间，结束时间小于开始时间
                if start >= time_end or end <= time_start:
                    course_form.save()
                    return HttpResponseRedirect('/courses_list/')
                else:
                    return HttpResponse('时间段冲突，请重新修改')
    else:
        course_form = CourseForm(instance=course)
    return render(request, 'training/course_edit.html', {'course_form': course_form})
