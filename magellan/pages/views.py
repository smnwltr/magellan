from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Imprint(TemplateView):
    template_name = 'imprint.html'


class Privacy(TemplateView):
    template_name = 'privacy.html'
