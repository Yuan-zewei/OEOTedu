from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_course/',views.show_course,name='show_course'),
    path('show_list/<int:id>/',views.show_list,name='show_list'),
    path('all_student/',views.all_student,name='all_student'),


]
