from django.shortcuts import render

from courses.models import Course
from blog.models import Post


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html',{"courses":courses})