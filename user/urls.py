# from django.contrib.auth.decorators import login_required
from django.urls import include, path

from . import views

app_name = "user"
urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("", views.login, name="login"),
]