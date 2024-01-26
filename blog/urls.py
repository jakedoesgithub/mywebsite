from django.urls import path
from . import views

app_name = "blog"

# thsi is a stand in to prevent breaking in other parts of app until i get around to configuring this part
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="home"),
    path(
        "author-detail/<slug:slug>/",
        views.AuthorDetailView.as_view(),
        name="author-detail",
    ),
    path(
        "recipe-detail/<slug:slug>/",
        views.RecipeDetailView.as_view(),
        name="recipe-detail",
    ),
    path("author-list/", views.AuthorListView.as_view(), name="latest_post"),
    path("about/", views.AboutCookbookView.as_view(), name="archive"),
]
