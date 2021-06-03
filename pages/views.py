from django.views.generic import TemplateView

class HomePageView(TemplateView): # héritage
    template_name = 'home.html' # le fichier template

class AboutPageView(TemplateView):
    template_name = 'about.html'
