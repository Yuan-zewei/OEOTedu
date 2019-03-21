from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('post_add/',views.post_add,name='post_add')
=======
    path('post/<int:id>/', views.post_list,name='post_list')
>>>>>>> origin/master

]
