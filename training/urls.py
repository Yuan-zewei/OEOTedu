from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_add/', views.post_add, name='post_add'),
    path('post/detail/<int:id>/', views.post_detail, name='post_detail'),
    path('post/update/<int:id>/', views.post_update, name='post_update'),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    ##部门以及部门详情 ————薛斌
    path('post/section_list/', views.section_list, name='section_list'),
    path('post/section_details/<int:id>/',views.section_details,name='section_details'),
    path('company/', views.company, name='company'),
    #     # 班级详细介绍----王帅
    path('class_list/', views.class_list, name='class_list'),   # 班级列表
    path('class_detail/<int:class_id>/', views.class_detail, name='class_detail'),  # 班级详情

]
