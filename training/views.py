from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Profile, Post
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'training/index.html', {'posts': posts})

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


def post_update(request, id):
    user = request.user
    post=Post.objects.get(id=id)
    # 判断用户是否有权限更改公告
    if user.profile.job == 'staff':
        # 获取想要更改公告的id找到此公告
        if request.method == "POST":
            # 获取方式POST
            form = PostForm(request.POST,instance=post)
            if form.is_valid():  # 是否合格
                form.save()
                return redirect("index")  # 返回主界面
        else:
            form = PostForm(instance=post)
        return render(request, 'training/post_update.html', {'form': form})
        # 如果用户没有权限
    else:
        # 弹出警告
        return HttpResponseRedirect('当前用户没有权限进行修改请切换用户或者联系管理员')
