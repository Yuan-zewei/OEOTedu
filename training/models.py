"""
文件：models.py
作者：OEOTedu
时间：2019-03-21
版本：0.1
email：40063539@qq.com
联系方式：QQ：40063539 电话：15903111958
"""

from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
# 公司表
class Company(models.Model):
    """
    定了一个公司类
    参数：
    name:公司名
    info：公司介绍
    """
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name


# 部门

class Department(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='departments')

    def __str__(self):
        return self.name


# 职位表
class Position(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name


# 个人信息

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女")
    )
    JOB_CHOICES = (
        ('staff', "职工"),
        ('student', "学生")
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=11)
    email = models.EmailField()
    entry = models.DateField()
    leave = models.DateField(blank=True, null=True)
    cardnumber = models.CharField(max_length=20, blank=True)
    idnumber = models.CharField(max_length=12, blank=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)
    job = models.CharField(max_length=7, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='depart_emp')
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name='position_emp')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    def __str__(self):
        return self.name


# 课程
class Course(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    most = models.PositiveSmallIntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='course')
    students = models.ManyToManyField(Profile, related_name='courses', blank=True)


# 考勤内容

class Duty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# 考勤信息
class Note(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='notes')
    dutys = models.ForeignKey(Duty, on_delete=models.CASCADE, related_name='notes')


# 文章
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    auth = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name='posts')
    publish = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


# 日志
class Logging(models.Model):
    login = models.DateTimeField()
    logout = models.DateTimeField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name='loggings')



