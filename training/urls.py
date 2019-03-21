from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_add/',views.post_add,name='post_add'),
    path('post/detail/<int:id>/',views.post_detail,name='post_detail'),
    path('post/update/<int:id>/',views.post_update,name='post_update')

]
