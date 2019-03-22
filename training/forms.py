from django.forms import ModelForm
from .models import Course

'''
添加文章时显示的字段
'''


class CourseCreate(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'info', 'most', 'starttime', 'endtime', 'teacher',)
