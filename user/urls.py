from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "user"
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("mypage/", views.mypage, name="mypage"),
    path("forgot/", views.forgot, name="forgot"),
]
