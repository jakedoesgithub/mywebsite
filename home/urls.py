from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("index/", views.IndexView.as_view(), name="index"),
]

urlpatterns += staticfiles_urlpatterns()
