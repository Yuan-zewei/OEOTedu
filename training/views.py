from django.shortcuts import render
from .models import Profile, Post


# Create your views here.
# 在主页查询文章作者
def index(request):
    posts = Profile.objects.all()
    return render(request, 'training/index.html', {'posts': posts})


# 在列表里获得到作者、内容和标题
def post_list(request, id):
    cat = Post.objects.get(id=id)
    return render(request, 'training/post_list.html', {'cat': cat})



