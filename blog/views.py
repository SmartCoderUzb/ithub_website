from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts":posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post":post})