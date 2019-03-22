from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseCreate
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


def register(request):
    return render(request, 'training/issue.html')


# 添加课程--赵昊蓁
def coursecreate(request):
    course = Course.objects.filter(teacher__name=request.user.profile.name)
    if request.method == 'POST':
        form = CourseCreate(data=request.POST)
        if form.is_valid() and course:
            # 获取的文章是所有，所以要for循环列出来一个一个判断
            for a in course:
                time_start = a.starttime
                time_end = a.endtime
                start_time = form.cleaned_data['starttime']
                start_end = form.cleaned_data['endtime']
                if start_time >= time_end or start_end <= time_start:
                    form.save()
                    return render(request, 'training/issue.html')
    else:
        form = CourseCreate()
    return render(request, 'training/create_course.html', {'form': form})


def abc(request):
    a = Course.objects.all()
    return render(request, 'training/course_list.html', {'a': a})


# 课程修改功能___远泽伟
def course_edit(request, id):
    course = Course.objects.get(id=id)
    courses = Course.objects.all().filter(teacher__name=request.user.profile.name)
    if request.method == 'POST':
        course_form = CourseCreate(data=request.POST, instance=course)
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
                    return redirect('course_list')
                else:
                    return HttpResponse('时间段冲突，请重新修改')
    else:
        course_form = CourseCreate(instance=course)
    return render(request, 'training/course_edit.html', {'course_form': course_form})


# 课程删除功能--赵昊蓁
def course_delete(request, id):
    affirm = Course.objects.get(id=id)
    affirm.delete()
    return redirect('course_list')
