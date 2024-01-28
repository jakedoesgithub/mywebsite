from django.shortcuts import render

# Create your views here.
# TODO Blog views


# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cookbook.models import Author, Recipe


# these cookbook views are a stand in to prevent breaking in other parts of app until i get around to configuring this part


class AboutCookbookView(TemplateView):
    template_name = "cookbook/about-cookbook.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "cookbook/author-detail.html"
    context_object_name = "author"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "cookbook/recipe-detail.html"
    context_object_name = "recipe"


class AuthorListView(ListView):
    model = Author
    template_name = "cookbook/author-list.html"
    context_object_name = "authors"


class RecipeListView(ListView):
    model = Recipe
    template_name = "cookbook/recipe-list.html"
    context_object_name = "recipes"
