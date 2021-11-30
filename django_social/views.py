from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "main_index.html"

