from django.db import models

from courses.models import Course


class Sertificat(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sertificates")