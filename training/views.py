from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import PostForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


def post_add(request):
    user = request.user
    #找到该用户
    if user.profile.job == 'staff':
        #判断该工作
        if request.method == "POST":
            #获取方式POST
            post_add = PostForm(request.POST)#找到该表单的内容
            if post_add.is_valid():#是否合格
                post_add.save()#保存
                return redirect("index")#返回主界面
        else:
            post_add = PostForm()#否则实例化对象
            return render(request, 'training/post_add.html', {'post_add': post_add})
    else:
        return HttpResponseRedirect("不能进行增加！！！")


#
