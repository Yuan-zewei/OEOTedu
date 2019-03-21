from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/update/<int:id>/', views.post_update, name='post_update'),
]
