from django.shortcuts import render

# Create your views here.


class CookbookHomeView(TemplateView):
    template_name = "cookbook_home.html"
