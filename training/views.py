from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Course


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


"""
文件：views.py
作者：赵猛彤
时间：2019-03-22
版本：0.1
email：1183525873@qq.com
联系方式：QQ：1183525873 电话：18931187921
"""


def course_list(request):  # 判断职务,分别进入页面__赵猛彤
    if request.user.profile.job == 'staff':
        # 显示该教师发布课程
        courses = Course.objects.all().filter(teacher__name=request.user.profile.name)
    else:
        # 显示该学生报名的课程
        courses = Course.objects.all().filter(students__name=request.user.profile.name)
    return render(request, 'training/course_list.html', {'courses': courses})
