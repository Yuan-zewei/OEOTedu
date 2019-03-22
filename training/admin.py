from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Profile, Position, Department, Company


# Register your models here.
@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'info']


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(Course)

# class Course(admin.ModelAdmin):
#     list_display = ['name']

@admin.register(Position)
class Position(admin.ModelAdmin):
    list_display = ['name', 'info']


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ['company']


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ['name', 'info']
