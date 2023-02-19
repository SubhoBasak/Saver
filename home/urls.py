from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.indexView, name='index'),
    path("home/", view=views.homeView, name='home'),
    path("capture/", view=views.captureView, name='capture'),
    path("register/", view=views.registerView, name='register'),
    path("login/", view=views.loginView, name='login'),
    path("logout/", view=views.LogoutView.as_view(), name='logout'),
    path("profile/", view=views.profileView, name='profile'),
]
