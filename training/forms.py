from django.forms import ModelForm
from .models import Course


# 课程修改的form模板
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'info', 'most', 'starttime', 'endtime', 'teacher')
