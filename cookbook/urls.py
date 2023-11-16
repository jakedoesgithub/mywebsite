from django.urls import path
from . import views

app_name = "cookbook"
urlpatterns = [
    path("", views.CookbookHomeView.as_view(), name="home"),
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
    path("recipe-list/", views.RecipeListView.as_view(), name="recipe-list"),
    path("about/", views.AboutCookbookView.as_view(), name="about-cookbook"),
]
