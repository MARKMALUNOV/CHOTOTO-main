from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.log.as_view(), name="login"),
    path("login/", views.log.as_view(), name="login"),
    path("register/", views.reg.as_view(), name="register"),
    path("app/", views.main.as_view(), name="app"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view.as_view(), name="profile"),
    path("stats/", views.stats_view.as_view(), name="stats"),
    path("add-habit/", views.add_habit, name="add_habit"),
]