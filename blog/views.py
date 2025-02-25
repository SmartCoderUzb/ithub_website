from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {"posts":posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    cookie_name = f'visited_post_{post_id}'
    response = render(request, 'post_detail.html', {'post': post})
    
    if not request.COOKIES.get(cookie_name):
        post.visitors = post.visitors + 1
        post.save()
        post.refresh_from_db(fields=['visitors'])
        response.set_cookie(cookie_name, 'true', max_age=365*24*60*60)
    return response