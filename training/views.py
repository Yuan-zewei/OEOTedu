from django.shortcuts import render, redirect
from .models import Profile, Post, Company, Department
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
# 查找到作者
def index(request):
    posts = Post.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


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


# 查看部门__斌
def section_list(request):
    look = Department.objects.filter(name__contains="部")
    return render(request, 'training/look_section.html', {'look': look})


# 查看班级__斌
def section_class(request):
    cla = Department.objects.filter(name__contains='班')
    return render(request, 'training/section_class.html',{'cla':cla})


# 部门下的人员__斌
def section_details(request, id):
    sec = Department.objects.get(id=id)
    # cla =
    return render(request, 'training/section_details.html', {'sec': sec})
