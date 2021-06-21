from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "glue/about.html"

class HomeView(TemplateView):
    template_name = "glue/index.html"

