# from django.contrib.auth.decorators import login_required
from django.urls import include, path

from . import views

app_name = "post"
urlpatterns = [
    path("blog-list", views.blog_list, name="blog-list"),
    path("create-blog", views.create_blog, name="create-blog"),
    path("like-unlike-blog", views.like_unlike_blog, name="like-unlike-blog"),
]