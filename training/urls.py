from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 公司信息详情页__来自小罗
    path('company/', views.company, name='company')

]
