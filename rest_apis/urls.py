from django.urls import include, path
from rest_framework import routers

from .views.user import UserViewSet
from .views.post import PostViewSet

"""
    priority: To extend behaviour of DefaultRouter
    purpose: Somewhere trailing slash is required and somewhere not,
        to implement less error prone strategy let just set trailing slash optional
"""


class OptionalSlashDefaultRouter(routers.DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = "/?"


router = OptionalSlashDefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("post", PostViewSet, basename="post")

urlpatterns = [path("", include(router.urls))]
