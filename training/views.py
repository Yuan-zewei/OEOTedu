from django.shortcuts import render, redirect
from . forms import PostForm
from .models import Profile, Post
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


def post_update(request, id):
    # 判断用户是否有权限更改公告
    user = request.user
    # 若果用户拥有权限
    if user.profile.job == 'staff':
        # 获取想要更改公告的id找到此公告
        post = Post.objects.get(id=id)
        # 如果获取到输入的内容
        if request.method == 'POST':
            # 获取到输入信息及原本自带信息
            form = PostForm(data=request.POST, instance=post)
            # 如果获取到的信息合法
            if form.is_valid():
                # 保存内容
                form.save()
                # 跳转页面到主页
                return redirect('index')
        # 如果没有获取到内容
        else:
            form = PostForm(instance=post)
        return render(request, 'training/post_update.html', {'form': form})
    # 如果用户没有权限
    else:
        # 弹出警告
        return HttpResponseRedirect('当前用户没有权限进行修改请切换用户或者联系管理员')
