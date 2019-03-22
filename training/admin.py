from django.contrib import admin
from .models import Post, Profile, Position, Department, Company, Note, Duty


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')


@admin.register(Department)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'company')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'info',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('starttime', 'endtime', 'profile')


@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_display = ('name', 'info',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('starttime', 'endtime', 'profile',)


@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ('name',)
