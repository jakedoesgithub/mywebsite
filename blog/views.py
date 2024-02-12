from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.models import Post


class BlogHomeView(TemplateView):
    template_name = "blog/blog-home.html"


class LastestPostView(TemplateView):
    template_name = "blog/latest-post.html"


class PostArchiveView(TemplateView):
    template_name = "blog/archive.html"


class TempPostView(TemplateView):
    template_name = "blog/temp-post.html"
