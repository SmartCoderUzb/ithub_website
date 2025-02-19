from django.urls import path

from .views import blog, post_detail


urlpatterns = [
    path('', blog, name="blog"),
    path('detail/<int:post_id>/', post_detail, name="post-detail")
]