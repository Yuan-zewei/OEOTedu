from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm, PostForm
from datetime import datetime
from .models import Profile, Post, Company
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
# 主页
def index(request):
    posts = Post.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


# 课程列表
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'training/courses_list.html', {'courses': courses})


# 课程添加功能__赵昊蓁
def course_add(request):
    courses = Course.objects.all().filter(teacher__name=request.user.profile.name)
    if request.method == 'POST':
        course_form = CourseForm(data=request.POST)
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
        course_form = CourseForm()
    return render(request, 'training/create_course.html', {'course_form': course_form})


# 课程修改功能
def course_edit(request, id):
    course = Course.objects.get(id=id)
    # 该老师的所有课程
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


def course_delete(request, id):
    all = Course.objects.get(id=id)
    all.delete()
    return HttpResponseRedirect('/courses_list/')


def company(request):
    company = Company.objects.all()
    return render(request, 'training/company.html', {'company': company})


# 在列表里获得到作者、内容和标题

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'training/post_detail.html', {'post': post})


def post_add(request):
    user = request.user
    # 找到该用户
    if user.profile.job == 'staff':
        # 判断该工作
        if request.method == "POST":
            # 获取方式POST
            post_add = PostForm(request.POST)  # 找到该表单的内容
            if post_add.is_valid():  # 是否合格
                new_post = post_add.save(commit=False)
                new_post.auth = user.profile
                new_post.save()
                return redirect("index")  # 返回主界面
        else:
            post_add = PostForm()  # 否则实例化对象
            return render(request, 'training/post_add.html', {'post_add': post_add})
    else:
        return HttpResponseRedirect("不能进行增加！！！")


#
def post_update(request, id):
    user = request.user
    # 找到该用户
    post = Post.objects.get(id=id)
    if user.profile.job == 'staff':
        # 判断该工作
        if request.method == "POST":
            # 获取方式POST
            form = PostForm(request.POST, instance=post)  # 找到该表单的内容
            if form.is_valid():  # 是否合格
                form.save()
                return redirect("index")  # 返回主界面
        else:
            form = PostForm(instance=post)  # 否则实例化对象
            return render(request, 'training/post_update.html', {'form': form})
    else:
        return HttpResponseRedirect("非职工身份不能修改公告！")


# 删除——艾鹏
def post_delete(request, id):
    user = request.user
    if user.profile.job == 'staff':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('/')
    else:
        return HttpResponse('当前登录用户没有权限，请切换用户或者联系管理员.')


# 判断职务,分别进入页面__赵猛彤
def course_list(request):
    all_courses = Course.objects.all()
    if request.user.profile.job == 'staff':
        # 显示该教师发布课程
        courses = Course.objects.all().filter(teacher__name=request.user.profile.name)
    else:
        # 显示该学生报名的课程
        courses = Course.objects.all().filter(students__name=request.user.profile.name)
    return render(request, 'training/courses_list.html', {'courses': courses, 'all_courses': all_courses})


def course_delete_stu(request, id):
    course = Course.objects.get(id=id)
    course.students.remove(request.user.profile)
    return redirect('courses_list')
