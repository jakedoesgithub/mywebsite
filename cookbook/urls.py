from django.urls import path
from . import views

urlpatterns = [
    path("", views.CookbookHomeView.as_view(), name="home"),
    path("author/<slug:slug>/", AuthorDetailView.as_view(), name="author-detail"),
    path("recipe/<slug:slug>/", RecipeDetailView.as_view(), name="recipe-detail"),
]
