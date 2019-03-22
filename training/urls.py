from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='indexs'),
    path('course_list/', views.course_list, name='course_list'),  # 链接课程列表页
]
