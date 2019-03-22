from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_add/',views.post_add,name='post_add'),
    path('post/detail/<int:id>/',views.post_detail,name='post_detail'),
    path('post/update/<int:id>/',views.post_update,name='post_update'),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post/section_list/', views.section_list, name='section_list'),
    path('post/class/', views.section_class, name='section_class'),
    path('post/section_details/<int:id>/',views.section_details,name='section_details'),


]
