from django.shortcuts import render
from django.views.generic.base import TemplateView


class homeView(TemplateView):
    template_name = "home/index.html"
