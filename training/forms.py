"""
20190321
删除
艾鹏
"""
from .models import Post
from django.forms import ModelForm
from .models import Course, Post


# 课程修改的form模板
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'info', 'most', 'starttime', 'endtime', 'teacher')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
