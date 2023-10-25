from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
urlpatterns += staticfiles_urlpatterns()
