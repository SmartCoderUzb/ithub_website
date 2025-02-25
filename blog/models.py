from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=300)
    image = models.ImageField(upload_to="post_images/")
    body = RichTextField()
    visitors = models.IntegerField(default=0)