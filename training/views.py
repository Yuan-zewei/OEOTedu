from django.shortcuts import render, redirect
from .models import Profile, Post, Company
from .forms import PostForm
from django.http import HttpResponseRedirect


# Create your views here.
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
