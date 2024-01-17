from django.urls import path
from . import views

app_name = "cookbook"
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe-list"),
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
    path("author-list/", views.AuthorListView.as_view(), name="author-list"),
    path("about/", views.AboutCookbookView.as_view(), name="about-cookbook"),
]
