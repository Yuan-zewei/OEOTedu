"""
20190321
删除
艾鹏
"""
from .models import Post
from .models import Post, Note
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('starttime', 'endtime', 'profile', 'dutys',)
