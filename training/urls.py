from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('create_course/', views.coursecreate, name='create_course'),
    path('list/', views.abc, name='course_list'),
    path('course_edit/<int:id>/', views.course_edit, name='course_edit'),
    path('course_delete/<int:id>/', views.course_delete, name='course_delete'),
]
