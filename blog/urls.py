from django.urls import path
from . import views

app_name = "blog"

# thsi is a stand in to prevent breaking in other parts of app until i get around to configuring this part
urlpatterns = [
    path("", views.BlogHomeView.as_view(), name="home"),
    path("latest/", views.LastestPostView.as_view(), name="latest-post"),
    path("archive/", views.PostArchiveView.as_view(), name="archive"),
    path("temp-post/", views.TempPostView.as_view(), name="temp-post"),
]
