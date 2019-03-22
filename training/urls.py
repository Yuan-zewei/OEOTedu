from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses_list/', views.courses_list, name='courses_list'),
    path('course_edit/<int:id>/', views.course_edit, name='course_edit'),
]
