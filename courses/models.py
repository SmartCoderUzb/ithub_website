from django.db import models
from users.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="course_images/")
    difficulity_level = models.CharField(
        max_length=100,
        choices=[
            ("Boshlang'ich","Boshlang'ich"),
            ("Murakkab","Murakkab"),
            ("Yuqori","Yuqori")
        ]
    )
    summary = models.CharField(max_length=500)
    price = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return f"ID: {self.id}: Title: {self.title}"
    

class CourseUserEnroll(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="course_enrolls",
        null=True
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="enrolls",
        null=True
    )