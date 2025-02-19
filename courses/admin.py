from django.contrib import admin

# Register your models here.
from .models import Course, CourseUserEnroll

admin.site.register(Course)
admin.site.register(CourseUserEnroll)