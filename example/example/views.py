from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'user_assets/index.html'
