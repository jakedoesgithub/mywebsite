from typing import Any, Dict
from django.shortcuts import render
from django.template import Context, Template
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.models import Post


class BlogHomeView(TemplateView):
    template_name = "blog/blog-home.html"


class LastestPostView(TemplateView):
    template_name = "blog/latest-post.html"
    img = "{% static 'blog/images/temp-post/python-plance.png' %}"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        html = Post.objects.latest("date_posted").content
        context["latest_post"] = Post.objects.latest("date_posted").content
        return context


class PostArchiveView(TemplateView):
    template_name = "blog/archive.html"


class TempPostView(TemplateView):
    template_name = "blog/temp-post.html"
